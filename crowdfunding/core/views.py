from django.shortcuts import render, redirect
from .models import (
    Pesquisador,
    Projeto,
    Instituicao
)

from .forms import PesquisadorForm, ProjetoForm


def home(request):
    return render(request, 'core/index.html')


def lista_pesquisadores(request):
    pesquisadores = Pesquisador.objects.all()
    form = PesquisadorForm()
    data = {'pesquisadores':pesquisadores, 'form': form}
    return render(request, 'core/lista_pesquisadores.html', data)


def pesquisador_novo(request):
    form = PesquisadorForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pesquisadores')


def lista_projetos(request):
    projetos = Projeto.objects.all()
    form = ProjetoForm()
    data = {'projetos':projetos, 'form': form}
    return render(request, 'core/lista_projetos.html',data)


def projeto_novo(request):
    form = ProjetoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_projetos')


def lista_instituicoes(request):
    instituicoes = Instituicao.objects.all()
    return render(request, 'core/lista_instituicoes.html',{'instituicoes':instituicoes})