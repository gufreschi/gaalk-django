from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'home.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def login_user(request):
    if request.method == 'POST':
        nome_usuario = request.POST['nome_usuario']
        senha = request.POST['senha']
        usuario = authenticate(request, username=nome_usuario, password=senha)
        if usuario is not None:
            login(request, usuario)
            messages.success(request, ('Você está conectado!'))
            return redirect('home')
        else:
            messages.error(request, ('Aconteceu algum erro. Tente novamente...'))
            return redirect('login')

    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('Você foi desconectado...'))
    return redirect('login')