from django.forms import ModelForm
from .models import Pesquisador, Projeto

class PesquisadorForm(ModelForm):
    class Meta:
        model = Pesquisador
        fields = '__all__'

class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'