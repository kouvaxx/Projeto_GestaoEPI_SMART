from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Colaborador, Equipamento, Emprestimo
from .forms import ColaboradorForm, EquipamentoForm, EmprestimoForm
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomAuthenticationForm
from django.urls import reverse_lazy
from django.urls import reverse

class CustomLoginView(LoginView):
    template_name = 'core/login.html'
    authentication_form = CustomAuthenticationForm

class CustomLogoutView(LogoutView):
    # Garantir que o logout redirecione para a tela de login
    next_page = reverse_lazy('login')

    # Opcional: permitir que um clique GET realize o logout (ou mantenha POST nas templates por segurança)
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

from .forms import UserUpdateForm


class CustomPasswordChangeView(PasswordChangeView):
    """Agora atua como 'Alterar Usuario' - permite alterar username e/ou senha."""
    template_name = 'core/change_password.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('emprestimo_list')

    def get(self, request, *args, **kwargs):
        user = request.user
        form = UserUpdateForm(initial={'username': user.username})
        password_form = self.form_class(user=request.user)
        return render(request, self.template_name, {'form': form, 'password_form': password_form})

    def post(self, request, *args, **kwargs):
        user = request.user
        form = UserUpdateForm(request.POST)
        password_form = self.form_class(user=request.user, data=request.POST)

        updated = False

        # Handle username change
        if form.is_valid():
            new_username = form.cleaned_data.get('username')
            if new_username and new_username != user.username:
                # ensure username not taken
                from django.contrib.auth.models import User
                if User.objects.filter(username=new_username).exclude(pk=user.pk).exists():
                    form.add_error('username', 'Nome de usuário já em uso.')
                else:
                    user.username = new_username
                    user.save()
                    updated = True

        # Handle password change separately: if password fields filled, validate and set
        # We allow changing password alone or together with username.
        pwd = request.POST.get('new_password')
        confirm = request.POST.get('confirm_password')
        if pwd or confirm:
            # validate via UserUpdateForm already did the matching check
            if form.is_valid() and pwd:
                user.set_password(pwd)
                user.save()
                updated = True

        if updated:
            # If password changed we should re-login; redirect to login page
            return redirect(self.success_url)

        # If not updated, re-render with errors
        return render(request, self.template_name, {'form': form, 'password_form': password_form})


@login_required
def home(request):
    return redirect('emprestimo_list')

@login_required
def colaborador_list(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'core/colaborador_list.html', {'colaboradores': colaboradores})

@login_required
def colaborador_create(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('colaborador_list')
    else:
        form = ColaboradorForm()
    return render(request, 'core/colaborador_form.html', {'form': form})

@login_required
def colaborador_update(request, pk):
    colaborador = get_object_or_404(Colaborador, pk=pk)
    if request.method == 'POST':
        form = ColaboradorForm(request.POST, instance=colaborador)
        if form.is_valid():
            form.save()
            return redirect('colaborador_list')
    else:
        form = ColaboradorForm(instance=colaborador)
    return render(request, 'core/colaborador_form.html', {'form': form})

@login_required
def colaborador_delete(request, pk):
    colaborador = get_object_or_404(Colaborador, pk=pk)
    if request.method == 'POST':
        colaborador.delete()
        return redirect('colaborador_list')
    return render(request, 'core/colaborador_confirm_delete.html', {'colaborador': colaborador})

@login_required
def equipamento_list(request):
    equipamentos = Equipamento.objects.all()
    return render(request, 'core/equipamento_list.html', {'equipamentos': equipamentos})

@login_required
def equipamento_create(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipamento_list')
    else:
        form = EquipamentoForm()
    return render(request, 'core/equipamento_form.html', {'form': form})

@login_required
def equipamento_update(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        form = EquipamentoForm(request.POST, instance=equipamento)
        if form.is_valid():
            form.save()
            return redirect('equipamento_list')
    else:
        form = EquipamentoForm(instance=equipamento)
    return render(request, 'core/equipamento_form.html', {'form': form})

@login_required
def equipamento_delete(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        equipamento.delete()
        return redirect('equipamento_list')
    return render(request, 'core/equipamento_confirm_delete.html', {'equipamento': equipamento})

@login_required
def emprestimo_list(request):
    emprestimos = Emprestimo.objects.all()
    # calcular quantidade em uso (emprestada - devolvida) para uso nos templates
    for e in emprestimos:
        e.em_uso = e.quantidade_emprestada - e.quantidade_devolvida
    return render(request, 'core/emprestimo_list.html', {'emprestimos': emprestimos})

@login_required
@transaction.atomic
def emprestimo_create(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            emprestimo = form.save(commit=False)
            equipamento = emprestimo.equipamento
            if equipamento.quantidade_disponivel >= emprestimo.quantidade_emprestada:
                equipamento.quantidade_disponivel -= emprestimo.quantidade_emprestada
                equipamento.save()
                emprestimo.save()
                return redirect('emprestimo_list')
            else:
                form.add_error('quantidade_emprestada', 'Quantidade indisponível.')
    else:
        form = EmprestimoForm()
    return render(request, 'core/emprestimo_form.html', {'form': form})

@login_required
def emprestimo_update(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    if request.method == 'POST':
        form = EmprestimoForm(request.POST, instance=emprestimo)
        if form.is_valid():
            form.save()
            return redirect('emprestimo_list')
    else:
        form = EmprestimoForm(instance=emprestimo)
    return render(request, 'core/emprestimo_form.html', {'form': form})

@login_required
@transaction.atomic
def emprestimo_delete(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    if request.method == 'POST':
        if not emprestimo.data_devolucao:
            equipamento = emprestimo.equipamento
            equipamento.quantidade_disponivel += emprestimo.quantidade_emprestada
            equipamento.save()
        emprestimo.delete()
        return redirect('emprestimo_list')
    return render(request, 'core/emprestimo_confirm_delete.html', {'emprestimo': emprestimo})

@login_required
@transaction.atomic
def emprestimo_devolucao(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    # calcular quantidade em uso para o template
    emprestimo.em_uso = emprestimo.quantidade_emprestada - emprestimo.quantidade_devolvida
    if request.method == 'POST':
        if not emprestimo.devolvido:
            # quantidade_devolvida recebida do formulário deve ser o que está sendo devolvido agora (delta)
            # se o usuário enviar o total acumulado por engano, ajustamos para não exceder o restante
            try:
                requested_return = int(request.POST.get('quantidade_devolvida', 0))
            except (TypeError, ValueError):
                requested_return = 0

            if requested_return > 0:
                remaining_to_return = emprestimo.quantidade_emprestada - emprestimo.quantidade_devolvida
                # só devolver até o restante pendente
                delta = min(requested_return, remaining_to_return)
                if delta > 0:
                    equipamento = emprestimo.equipamento
                    equipamento.quantidade_disponivel += delta
                    equipamento.save()

                    emprestimo.quantidade_devolvida += delta
                    if emprestimo.quantidade_devolvida >= emprestimo.quantidade_emprestada:
                        emprestimo.devolvido = True
                        emprestimo.data_devolucao = timezone.now()
                    emprestimo.save()
        return redirect('emprestimo_list')
    # Se não for POST, mostrar formulário de devolução
    return render(request, 'core/emprestimo_devolucao.html', {'emprestimo': emprestimo})


@login_required
def ajuda_view(request):
    """Renderiza a página de ajuda com instruções de uso."""
    return render(request, 'core/ajuda.html')


def sobre_view(request):
    """Página pública 'Sobre' com informações do projeto."""
    return render(request, 'core/sobre.html')


