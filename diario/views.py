from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pessoa, Diario


def home(request):
    return render(request, 'home.html')


def escrever(request):
    if request.method == 'GET':
        pessoas = Pessoa.objects.all()
        return render(request, 'escrever.html', {'pessoas': pessoas})
    elif request.method == 'POST':
        titulo = request.POST.get('titulo')
        tags = request.POST.getlist('tags')
        pessoas = request.POST.getlist('pessoas')
        texto = request.POST.get('texto')

        if len(titulo.strip()) == 0 or len(texto.strip()) == 0:
            # TODO: Adicionar mensagens de erro
            return redirect('escrever')

        diario = Diario(
            titulo=titulo,
            texto=texto
        )
        diario.save()

        return HttpResponse(f'{titulo} - {tags} - {pessoas} - {texto}')


def cadastrar_pessoa(request):
    if request.method == 'GET':
        return render(request, 'pessoa.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        foto = request.FILES.get('foto')

        pessoa = Pessoa(
            nome=nome,
            foto=foto
        )
        pessoa.save()
        return redirect('escrever')
