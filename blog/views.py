from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Home
def home(request):
    return render(request, 'blog/home.html')

# Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

# Logout
def logout_view(request):
    logout(request)
    return redirect('home')

# Cadastro
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Conta criada com sucesso! Faça login.")
            return redirect('login')
        else:
            messages.error(request, "Erro ao criar a conta.")
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

# Perfil (apenas logados)
@login_required
def profile(request):
    return render(request, 'blog/profile.html')

# Recuperar senha (placeholder)
def password_reset(request):
    return render(request, 'blog/password_reset.html')

# Alterar senha (placeholder)
@login_required
def password_change(request):
    return render(request, 'blog/password_change.html')

# Handlers de erro
def error_404_view(request, exception):
    return render(request, 'blog/404.html', status=404)

def error_403_view(request, exception):
    return render(request, 'blog/403.html', status=403)

def error_500_view(request):
    return render(request, 'blog/500.html', status=500)
