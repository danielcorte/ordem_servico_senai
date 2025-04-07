from django.db import models

# Create your models here.

class Gestores(models.Model):
    ni = models.CharField()
    nome = models.CharField()
    area = models.CharField()
    cargo = models.CharField()

