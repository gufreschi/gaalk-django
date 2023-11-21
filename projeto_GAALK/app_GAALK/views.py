from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html', {})

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        # data_nascimento = request.POST.get('data_nascimento')
        # telefone = request.POST.get('telefone')
        senha1 = request.POST.get('senha1')
        senha2 = request.POST.get('senha2')
        
        user = User.objects.filter(username=username).first()
        if user:
            messages.error(request, ('Esse nome de usuário já existe'))
            return redirect('cadastro')
        
        if senha1 == senha2:
            user = User.objects.create_user(username=username, email=email, password=senha1)
            user.save()
            messages.success(request, ('Cadastro realizado com sucesso!'))
            return redirect('login')
        else:
            messages.error(request, ('As senhas devem ser iguais.'))
            return redirect('cadastro')
    else:
        return render(request, 'cadastro.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha1 = request.POST['senha1']
        user = authenticate(request, username=username, password=senha1)
        if user is not None:
            login(request, user)
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