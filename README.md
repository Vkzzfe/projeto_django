# Projeto Django Blog

Este é um projeto em Django com páginas de autenticação (login, logout, cadastro, perfil e recuperação de senha) e tratamento personalizado de erros (404, 403 e 500). O app principal é `blog`, configurado na raiz do projeto, com templates básicos para navegação entre as páginas.

## Funcionalidades
- Página inicial (Home)
- Login e Logout
- Cadastro de usuário
- Recuperação e alteração de senha
- Página de perfil
- Páginas personalizadas de erro

## Tecnologias
- Python 3.x
- Django 5.x
- HTML5 / CSS3 (templates)

## Como rodar o projeto
1. Clone este repositório:
   ```bash
   git clone https://github.com/vkzzfe/projeto_django.git
Crie e ative o ambiente virtual:

bash
Copiar código
python -m venv venv
venv\Scripts\activate  # Windows
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Rode o servidor:

bash
Copiar código
python manage.py runserver
Acesse em: http://localhost:8000
