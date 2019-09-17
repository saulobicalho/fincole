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


def pesquisador_update(request, id):
    data = {}
    pesquisador = Pesquisador.objects.get(id=id)
    form = PesquisadorForm(request.POST or None, instance=pesquisador)
    data['pesquisador'] = pesquisador
    data['form'] = form

    if request.method =='POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pesquisadores')
    else:
        return render(request, 'core/update_pesquisador.html',data)


def pesquisador_delete(request, id):
    data = {}
    pesquisador = Pesquisador.objects.get(id=id)
    if request.method == 'POST':
        pesquisador.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html',{'pesquisador':pesquisador})


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


def projeto_update(request, id):
    data = {}
    projeto = Projeto.objects.get(id=id)
    form = ProjetoForm(request.POST or None, instance=projeto)
    data['projeto'] = projeto
    data['form'] = form

    if request.method =='POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_projetos')
    else:
        return render(request, 'core/update_projeto.html',data)


def lista_instituicoes(request):
    instituicoes = Instituicao.objects.all()
    return render(request, 'core/lista_instituicoes.html',{'instituicoes':instituicoes})