from django.contrib import admin
from .models import Post  # importa o modelo que você criou

# Registra o modelo para aparecer no Django Admin
admin.site.register(Post)
