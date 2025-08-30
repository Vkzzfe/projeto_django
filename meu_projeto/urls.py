from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # app na raiz
]

# Handlers de erro
handler404 = 'blog.views.error_404_view'
handler403 = 'blog.views.error_403_view'
handler500 = 'blog.views.error_500_view'
