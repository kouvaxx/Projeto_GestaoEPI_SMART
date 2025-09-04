from django import forms
from .models import Colaborador, Equipamento, Emprestimo

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['nome_completo', 'matricula', 'funcao', 'data_admissao']
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control'}),
            'funcao': forms.TextInput(attrs={'class': 'form-control'}),
            'data_admissao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['nome_epi', 'descricao', 'quantidade_total', 'quantidade_disponivel']
        widgets = {
            'nome_epi': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'quantidade_total': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantidade_disponivel': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class EmprestimoForm(forms.ModelForm):
    colaborador = forms.ModelChoiceField(
        queryset=Colaborador.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    equipamento = forms.ModelChoiceField(
        queryset=Equipamento.objects.filter(quantidade_disponivel__gt=0),
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Emprestimo
        fields = ['colaborador', 'equipamento', 'quantidade_emprestada']
        widgets = {
            'quantidade_emprestada': forms.NumberInput(attrs={'class': 'form-control'}),
        }


from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserUpdateForm(forms.Form):
    username = forms.CharField(required=False, max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    new_password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned = super().clean()
        pwd = cleaned.get('new_password')
        confirm = cleaned.get('confirm_password')
        if pwd or confirm:
            if pwd != confirm:
                raise forms.ValidationError('As senhas não coincidem.')
        return cleaned