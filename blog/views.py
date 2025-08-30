from django.shortcuts import render
from django.http import HttpResponse

# Home
def home(request):
    return render(request, 'blog/home.html')

# Login
def login_view(request):
    return render(request, 'blog/login.html')

# Logout
def logout_view(request):
    return render(request, 'blog/logout.html')

# Cadastro
def register(request):
    return render(request, 'blog/register.html')

# Recuperar senha
def password_reset(request):
    return render(request, 'blog/password_reset.html')

# Alterar senha
def password_change(request):
    return render(request, 'blog/password_change.html')

# Perfil
def profile(request):
    return render(request, 'blog/profile.html')

def error_404_view(request, exception):
    return render(request, "404.html", status=404)

def error_403_view(request, exception):
    return render(request, 'blog/403.html', status=403)

def error_500_view(request):
    return render(request, 'blog/500.html', status=500)
