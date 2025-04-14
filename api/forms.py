from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models_user import Usuario

class FormCadastro(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2', 'nivel']

class FormLogin(AuthenticationForm):
    username = forms.CharField(label="Usuário ou Email")

    