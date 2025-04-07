from django.db import models

# Create your models here.

class Gestores(models.Model):
    ni = models.CharField()
    nome = models.CharField()
    area = models.CharField()
    cargo = models.CharField()

class Manutentores(models.Model):
    ni = models.CharField()
    nome = models.CharField()
    area = models.CharField()
    gestor = models.ForeignKey(Gestores, on_delete=models.CASCADE)

class Patrimonios(models.Model):
    ni = models.CharField()
    descricao = models.CharField()
    localizacao = models.CharField()

class Ambientes(models.Model):
    ni = models.CharField()
    nome = models.CharField()
    responsavel = models.CharField()
