"""crowdfunding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import home
from pesquisadores.views import pesquisadores, pesquisador_detalhe, pesquisador_por_nome

urlpatterns = [
    path('',home),
    path('pesquisadores',pesquisadores),
    url('pesquisador/(?P<id>\d+)$',pesquisador_detalhe),
    url('pesquisador/(?P<nome>\w+)$',pesquisador_por_nome),
    path('admin/', admin.site.urls),
]
