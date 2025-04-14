from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(models.Model):
    ni = models.CharField(max_length=15)
    nome = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    foto = models.ImageField()


class Usuario(AbstractUser):
    NIVEL_CHOICES = [
        ('admin', 'Administrador'),
        ('manutentor', 'Manutentor'),
        ('default', 'Default'),
    ]
    nivel = models.CharField(max_length=10, choices=NIVEL_CHOICES, default='default')