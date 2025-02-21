from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
import re

class RegisterForm(UserCreationForm):
    name = forms.CharField(
        max_length=150,
        label="Nome Completo",
        required=True,
        help_text="Insira seu nome completo.",
    )
    email = forms.EmailField(required=True)
    password1 = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput,
        help_text="A senha deve ter pelo menos 8 caracteres, uma letra maiúscula, um número e um caractere especial."
    )
    password2 = forms.CharField(label="Confirmar Senha", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ["name", "email", "password1", "password2"]

    def clean_name(self):
        nome = self.cleaned_data.get("name")
        
        # Permitir apenas letras e espaços
        if not re.match(r"^[A-Za-zÀ-ÿ\s]+$", nome):
            raise forms.ValidationError("O nome deve conter apenas letras e espaços.")
        
        return nome

    def clean_password1(self):
        senha = self.cleaned_data.get("password1")
        if len(senha) < 8 or not re.search(r"[A-Z]", senha) or not re.search(r"\d", senha) or not re.search(r"\W", senha):
            raise forms.ValidationError("A senha deve atender aos requisitos mínimos.")
        return senha

    def clean_password2(self):
        senha1 = self.cleaned_data.get("password1")
        senha2 = self.cleaned_data.get("password2")
        if senha1 and senha2 and senha1 != senha2:
            raise forms.ValidationError("As senhas não coincidem.")
        return senha2

    def save(self, commit=True):
        """Salva o usuário com o nome e gera o username automaticamente."""
        user = super().save(commit=False)
        user.name = self.cleaned_data["name"] 
        
        if commit:
            user.save()
        return user
