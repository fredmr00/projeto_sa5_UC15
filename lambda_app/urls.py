from django.urls import path
from lambda_app.views import index, listar, deletar_registro, registrar_aluno

urlpatterns = [
    # Cadastrar URLs aqui
    path('', index),
    path('listar/', listar), 
]
