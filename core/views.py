from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect

import git  # type: ignore

# Atualização do repositório via webhook (opcional)
@csrf_exempt
def update(request):
    if request.method == "POST":
        repo = git.Repo('/home/drsantos20/bookstore')  # 🔴 Atenção: esse caminho pode estar incorreto!
        origin = repo.remotes.origin
        origin.pull()
        return HttpResponse("Updated code on PythonAnywhere")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")

# View de exemplo com template
def hello_world(request):
    template = loader.get_template('hello_world.html')
    return HttpResponse(template.render())

# ========== VIEWS REQUISITADAS PELO urls.py ==========

def login_view(request):
    return HttpResponse("Página de login")

def register(request):
    return HttpResponse("Página de registro")

def create_tweet(request):
    return HttpResponse("Criar tweet")

def delete_tweet(request, id):
    return HttpResponse(f"Excluir tweet com ID {id}")

def logout_view(request):
    return HttpResponse("Logout do usuário")

def feed_view(request):
    return HttpResponse("Feed de tweets")

def home(request):
    return HttpResponse("Página inicial")