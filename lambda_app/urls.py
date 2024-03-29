from django.urls import path
from lambda_app.views import index, listar, deletar_registro, registrar_aluno, atualizar_registro, pesquisa_aluno, pesquisa_cpf

urlpatterns = [
    # Cadastrar URLs aqui
    path('', index),
    path('listar/', listar),
    path('deletar_registro/', deletar_registro),
    path('registrar_aluno/', registrar_aluno),
    path('atualizar_registro/', atualizar_registro),
    path('pesquisa_aluno/', pesquisa_aluno),
    path('pesquisa_cpf/', pesquisa_cpf),
]
