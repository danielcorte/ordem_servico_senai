from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrador'),
        ('manutentor', 'Manutentor'),
        ('gestor', 'Gestor'),
        ('default', 'Default'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='default')

class Gestores(models.Model):
    ni = models.CharField(max_length=15)
    nome = models.CharField(max_length=64)
    area = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)

class Manutentores(models.Model):
    ni = models.CharField(max_length=15)
    nome = models.CharField(max_length=64)
    area = models.CharField(max_length=255)
    gestor = models.ForeignKey(Gestores, on_delete=models.CASCADE)



class Patrimonios(models.Model):
    ni = models.CharField(max_length=15)
    descricao = models.CharField(max_length=255)
    localizacao = models.CharField(max_length=255)

class Ambientes(models.Model):
    ni = models.CharField(max_length=15)
    nome = models.CharField(max_length=64)
    responsavel = models.CharField(max_length=255)

class OrdemServico(models.Model):
    STATUS = {
        "andamento": "Andamento",
        "concluido": "Concluído",
        "cancelado": "Cancelado",
        "aberto": "Aberto"
    }

    PRIORIDADE = {
        "alta": "Alta",
        "media": "Media",
        "baixa": "Baixa"
    }

    descricao = models.CharField(max_length=255),
    abertura = models.DateTimeField(),
    fechamento = models.DateTimeField(),
    status = models.CharField(max_length=10, choices=STATUS),
    patrimonio = models.ForeignKey(Patrimonios, on_delete=models.CASCADE)
    ambiente = models.ForeignKey(Ambientes, on_delete=models.CASCADE)
    manutentor = models.ForeignKey(Manutentores, on_delete=models.CASCADE)
    responsavel = models.CharField(max_length=255),
    prioridade = models.CharField(max_length=5, choices=PRIORIDADE)

