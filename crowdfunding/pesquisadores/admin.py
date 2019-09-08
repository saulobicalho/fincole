from django.contrib import admin
from .models import Pesquisador, Instituicao, Projeto

class PesquisadorAdmin(admin.ModelAdmin):
    list_display = ('nome','instituicao_origem')
    list_filter = ('instituicao_origem',)

admin.site.register(Pesquisador, PesquisadorAdmin)
admin.site.register(Instituicao)
admin.site.register(Projeto)