from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.register_user, name='cadastro'),
    path('login/', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('sobre/', views.sobre, name='sobre'),
]