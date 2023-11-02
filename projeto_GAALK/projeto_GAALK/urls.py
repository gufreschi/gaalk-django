from django.contrib import admin
from django.urls import path
from app_GAALK import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),\
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
]