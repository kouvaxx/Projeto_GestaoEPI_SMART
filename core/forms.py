from django import forms
from .models import Colaborador, Equipamento, Emprestimo, Perfil
from django.contrib.auth.models import User

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

class PerfilUpdateForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['foto']

from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'})
        }
