from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import Perfil
from .forms import UserEditForm, PerfilEditForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Crear perfil automáticamente para el nuevo usuario
            Perfil.objects.create(user=user)
            login(request, user)
            return redirect('inicio')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {'user': request.user})

@login_required
def edit_profile(request):
    user_form = UserEditForm(instance=request.user)
    perfil_form = PerfilEditForm(instance=request.user.perfil)
    
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        perfil_form = PerfilEditForm(request.POST, request.FILES, instance=request.user.perfil)
        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            return redirect('profile')
    
    return render(request, 'accounts/edit_profile.html', {
        'user_form': user_form,
        'perfil_form': perfil_form
    })

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Mantiene la sesión activa
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})