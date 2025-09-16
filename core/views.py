from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Colaborador, Equipamento, Emprestimo, Perfil
from .forms import ColaboradorForm, EquipamentoForm, EmprestimoForm, UserUpdateForm, PerfilUpdateForm
from django.db import transaction
from django.db import transaction, models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm # Import SetPasswordForm
from .forms import CustomAuthenticationForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.http import JsonResponse
from collections import defaultdict
from django.contrib.auth.models import User # Ensure User model is imported

class CustomLoginView(LoginView):
    template_name = 'core/login.html'
    authentication_form = CustomAuthenticationForm

    def form_valid(self, form):
        messages.success(self.request, 'Login bem-sucedido!')
        return super().form_valid(form)

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'Logout bem-sucedido!')
        return super().dispatch(request, *args, **kwargs)

@login_required
def home(request):
    return redirect('emprestimo_list')

@login_required
def colaborador_list(request):
    query = request.GET.get('q')
    colaboradores_list = Colaborador.objects.all().order_by('nome_completo')
    if query:
        colaboradores_list = colaboradores_list.filter(
            Q(nome_completo__icontains=query) | Q(matricula__icontains=query)
        )

    paginator = Paginator(colaboradores_list, 10)  # 10 itens por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'core/colaborador_list.html', {'page_obj': page_obj})

@login_required
def colaborador_create(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Colaborador criado com sucesso!')
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
            messages.success(request, 'Colaborador atualizado com sucesso!')
            return redirect('colaborador_list')
    else:
        form = ColaboradorForm(instance=colaborador)
    return render(request, 'core/colaborador_form.html', {'form': form})

@login_required
def colaborador_delete(request, pk):
    colaborador = get_object_or_404(Colaborador, pk=pk)
    if request.method == 'POST':
        colaborador.delete()
        messages.success(request, 'Colaborador excluído com sucesso!')
        return redirect('colaborador_list')
    return render(request, 'core/colaborador_confirm_delete.html', {'colaborador': colaborador})

@login_required
def equipamento_list(request):
    query = request.GET.get('q')
    equipamentos_list = Equipamento.objects.all().order_by('nome_epi')
    if query:
        equipamentos_list = equipamentos_list.filter(nome_epi__icontains=query)

    paginator = Paginator(equipamentos_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'core/equipamento_list.html', {'page_obj': page_obj})

@login_required
def equipamento_create(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipamento criado com sucesso!')
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
            messages.success(request, 'Equipamento atualizado com sucesso!')
            return redirect('equipamento_list')
    else:
        form = EquipamentoForm(instance=equipamento)
    return render(request, 'core/equipamento_form.html', {'form': form})

@login_required
def equipamento_delete(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        equipamento.delete()
        messages.success(request, 'Equipamento excluído com sucesso!')
        return redirect('equipamento_list')
    return render(request, 'core/equipamento_confirm_delete.html', {'equipamento': equipamento})

@login_required
def emprestimo_list(request):
    query = request.GET.get('q')
    emprestimos_list = Emprestimo.objects.all().order_by('-data_emprestimo')
    if query:
        emprestimos_list = emprestimos_list.filter(
            Q(colaborador__nome_completo__icontains=query) | Q(equipamento__nome_epi__icontains=query)
        )
    # calcular quantidade em uso (emprestada - devolvida) para uso nos templates
    for e in emprestimos_list:
        e.em_uso = e.quantidade_emprestada - e.quantidade_devolvida

    paginator = Paginator(emprestimos_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'core/emprestimo_list.html', {'page_obj': page_obj})

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
                messages.success(request, 'Empréstimo criado com sucesso!')
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
            messages.success(request, 'Empréstimo atualizado com sucesso!')
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
        messages.success(request, 'Empréstimo excluído com sucesso!')
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
                    messages.success(request, 'Devolução registrada com sucesso!')
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

# New views for independent profile management
@login_required
def update_profile_picture(request):
    try:
        perfil_instance = request.user.perfil
    except Perfil.DoesNotExist:
        perfil_instance = Perfil.objects.create(user=request.user)

    if request.method == 'POST':
        perfil_form = PerfilUpdateForm(request.POST, request.FILES, instance=perfil_instance)
        if perfil_form.is_valid():
            perfil_form.save()
            messages.success(request, 'Sua foto de perfil foi atualizada com sucesso!')
            return redirect('update_profile_picture')
        else:
            messages.error(request, 'Erro ao atualizar a foto de perfil. Verifique os dados.')
    else:
        perfil_form = PerfilUpdateForm(instance=perfil_instance)
    
    context = {
        'perfil_form': perfil_form
    }
    return render(request, 'core/update_profile_picture.html', context)

@login_required
def update_username(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Seu nome de usuário foi atualizado com sucesso!')
            return redirect('update_username')
        else:
            messages.error(request, 'Erro ao atualizar o nome de usuário. Verifique os dados.')
    else:
        user_form = UserUpdateForm(instance=request.user)
    
    context = {
        'user_form': user_form
    }
    return render(request, 'core/update_username.html', context)

@login_required
def update_password(request):
    if request.method == 'POST':
        password_form = SetPasswordForm(request.user, request.POST)
        if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request, password_form.user) # Important to keep the user logged in
            messages.success(request, 'Sua senha foi atualizada com sucesso!')
            return redirect('update_password')
        else:
            messages.error(request, 'Erro ao atualizar a senha. Verifique os dados.')
    else:
        password_form = SetPasswordForm(request.user)
    
    context = {
        'password_form': password_form
    }
    return render(request, 'core/update_password.html', context)

@login_required
def profile_settings(request):
    return render(request, 'core/profile_settings.html')