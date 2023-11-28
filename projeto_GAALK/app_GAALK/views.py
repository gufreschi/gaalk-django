from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import requests
import datetime

def home(request):
    api_key = '57f14addda3858ec4ab6c57f9ed23f2c'
    base_url = 'https://api.themoviedb.org/3/discover/movie'

    current_year = datetime.date.today().year

    params = {
        'api_key': api_key,
        'primary_release_year': current_year,
        'sort_by': 'vote_count.desc',
        'language': 'pt-br',
        'page': 1,
        'per_page': 20,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()       
        posters = [result['poster_path'] for result in data.get('results', [])]
        titles = [result['title'] for result in data.get('results', [])]
        ratings = [result['vote_average'] for result in data.get('results', [])]
        votes = [result['vote_count'] for result in data.get('results', [])]
        overviews = [result['overview'] for result in data.get('results', [])]
        
        context = {'posters': zip(posters, titles, ratings, votes, overviews), 'current_year': current_year}
        return render(request, 'home.html', context)
    
    else:
        return redirect('error')
    
def search(request):
    api_key = '57f14addda3858ec4ab6c57f9ed23f2c'
    base_url = 'https://api.themoviedb.org/3/search/movie'

    query = request.GET.get('query', '')

    params = {
        'api_key': api_key,
        'query': query,
        'language': 'pt-br',
        'page': 1,
        'per_page': 20,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        posters = [result['poster_path'] for result in data.get('results', [])]
        titles = [result['title'] for result in data.get('results', [])]
        ratings = [result['vote_average'] for result in data.get('results', [])]
        votes = [result['vote_count'] for result in data.get('results', [])]
        overviews = [result['overview'] for result in data.get('results', [])]

        context = {'posters': zip(posters, titles, ratings, votes, overviews), 'query': query}
        return render(request, 'search.html', context)
    
    else:
        return redirect('error')
    
def descobrir(request):
    pass

def sobre(request):
    return render(request, 'sobre.html', {})

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
            messages.error(request, ('Nome indisponível.'))
            return redirect('cadastro')
        
        if senha1 == senha2:
            user = User.objects.create_user(username=username, email=email, password=senha1)
            user.save()
            messages.success(request, ('Cadastro realizado!'))  
            return redirect('login')
        else:
            messages.error(request, ('As senhas não coincidiram.'))
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
            messages.error(request, ('Erro. Tente Novamente...'))
            return redirect('login')

    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('Você foi desconectado...'))
    return redirect('login')

def error(request):
    return render(request, 'error.html')