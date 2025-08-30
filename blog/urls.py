from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('password-reset/', views.password_reset, name='password_reset'),
    path('password-change/', views.password_change, name='password_change'),
    path('profile/', views.profile, name='profile'),
]
