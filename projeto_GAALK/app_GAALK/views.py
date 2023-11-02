from django.shortcuts import render
from .models import Usuario
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate

def home(request):
    return render(request,'usuarios/index.html')

def login(request):
    return render(request,'usuarios/login.html')

def cadastro(request):
    return render(request,'usuarios/cadastro.html')

def usuarios(request):
    # Salvar os dados da tela para o banco de dados.
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.cpf = request.POST.get('cpf')
    novo_usuario.data_nascimento = request.POST.get('data_nascimento')
    novo_usuario.telefone = request.POST.get('telefone')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.senha = request.POST.get('senha')
    novo_usuario.conf_senha = request.POST.get('conf_senha')
    novo_usuario.save()

    #Retornar para a pagina de login.
    return render(request, 'usuarios/login.html')