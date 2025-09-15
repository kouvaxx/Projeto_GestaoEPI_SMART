from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Colaborador(models.Model):
    nome_completo = models.CharField(max_length=255)
    matricula = models.CharField(max_length=50, unique=True)
    funcao = models.CharField(max_length=100)
    data_admissao = models.DateField()

    def __str__(self):
        return self.nome_completo

class Equipamento(models.Model):
    nome_epi = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    quantidade_total = models.PositiveIntegerField(default=0)
    quantidade_disponivel = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome_epi

class Emprestimo(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField(default=timezone.now)
    data_devolucao = models.DateTimeField(null=True, blank=True)
    devolvido = models.BooleanField(default=False)
    quantidade_emprestada = models.PositiveIntegerField(default=0)
    quantidade_devolvida = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.equipamento.nome_epi} para {self.colaborador.nome_completo}"

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Perfil'
