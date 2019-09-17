from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from .views import (
    home,
    lista_pesquisadores,
    pesquisador_novo,
    pesquisador_update,
    pesquisador_delete,
    lista_projetos,
    projeto_novo,
    projeto_update,
    projeto_delete,
    lista_instituicoes,
)
urlpatterns = [
    path('',home, name='core_home'),

    path('pesquisadores',lista_pesquisadores, name='core_lista_pesquisadores'),
    path('pesquisador-novo',pesquisador_novo, name='core_pesquisador_novo'),
    url('pesquisador-update/(?P<id>\d+)/$', pesquisador_update, name='core_pesquisador_update'),
    url('pesquisador-delete/(?P<id>\d+)/$', pesquisador_delete, name='core_pesquisador_delete'),

    path('projeto-novo',projeto_novo, name='core_projeto_novo'),
    path('projetos', lista_projetos, name='core_lista_projetos'),
    url('projeto-update/(?P<id>\d+)/$', projeto_update, name='core_projeto_update'),
    url('projeto-delete/(?P<id>\d+)/$', projeto_delete, name='core_projeto_delete'),

    path('instituicoes', lista_instituicoes, name='core_lista_instituicoes'),
]
