from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=200, null=False)
    cpf = models.CharField(max_length=14, null=False)
    email = models.EmailField(max_length=200, null=False)
    telefone = models.CharField(max_length=20, null=False)
