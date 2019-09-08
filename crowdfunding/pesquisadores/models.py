from django.db import models


class Instituicao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Pesquisador(models.Model):
    nome = models.CharField(max_length=70, null=False)
    email = models.EmailField()
    rg = models.CharField(max_length=12, null=False)
    cpf = models.CharField(max_length=15, null=False)
    instituicao_origem = models.ForeignKey(Instituicao, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    titulo = models.CharField(max_length=120, null=False)
    descricao = models.TextField(max_length=500)
    autor = models.ForeignKey(Pesquisador, on_delete=models.PROTECT)
    objetivo = models.IntegerField(null=False)
    arrecadado = models.IntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
