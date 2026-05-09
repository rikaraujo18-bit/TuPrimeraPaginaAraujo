from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
    biografia = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Perfil de {self.user.username}"