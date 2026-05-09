from django import forms
from django.contrib.auth.models import User
from .models import Perfil

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class PerfilEditForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['avatar', 'biografia']