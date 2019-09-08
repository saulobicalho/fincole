from django.shortcuts import render
from django.http import HttpResponse

def pesquisadores(request):
    return HttpResponse(' mostra os pesquisadores')

def pesquisador_detalhe(request,id):
    return HttpResponse(id)

def pesquisador_por_nome(request,nome):
    return HttpResponse(nome)
