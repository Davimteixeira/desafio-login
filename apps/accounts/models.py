import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=150, verbose_name="Nome Completo")
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']  

    def save(self, *args, **kwargs):
        """Gera automaticamente o username baseado no nome, removendo espaços."""
        if not self.username:  
            base_username = "".join(self.name.split()).lower()  
            username = base_username
            count = 1

            while CustomUser.objects.filter(username=username).exists():
                username = f"{base_username}{uuid.uuid4().hex[:4]}" 
            
            self.username = username

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.email})"
