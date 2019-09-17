from django.contrib import admin
from django.urls import path
from django.conf.urls import include


from .views import (
    home,
    lista_pesquisadores,
    lista_projetos,
    lista_instituicoes,
    pesquisador_novo,
    projeto_novo,
)
urlpatterns = [
    path('',home, name='core_home'),
    path('pesquisadores',lista_pesquisadores, name='core_lista_pesquisadores'),
    path('pesquisador-novo',pesquisador_novo, name='core_pesquisador_novo'),
    path('projeto-novo',projeto_novo, name='core_projeto_novo'),
    path('projetos', lista_projetos, name='core_lista_projetos'),
    path('instituicoes', lista_instituicoes, name='core_lista_instituicoes'),
]
