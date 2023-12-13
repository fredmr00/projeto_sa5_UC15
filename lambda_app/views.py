from django.shortcuts import render, get_object_or_404, redirect
from lambda_app.models import Aluno 
from lambda_app.forms import AlunoForm
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "lambda_app/partial/principal.html")

def listar(request):
    alunos = Aluno.objects.all()
    return render(request, 'lambda_app/partial/listar_alunos.html', {'alunos': alunos})

def registrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listar')
    else:
        form = AlunoForm()
    return render(request, 'lambda_app/partial/formulario_registro.html', {'form': form})

def atualizar_registro(request):
    aluno_id = request.GET.get('pk')
    aluno = get_object_or_404(Aluno, pk=aluno_id)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('/listar')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'lambda_app/partial/atualizar_registro.html', {'form': form})

def deletar_registro(request):
     aluno_id = request.GET.get('pk')
     aluno = get_object_or_404(Aluno, pk=aluno_id)
     if request.method == 'POST':
         aluno.delete()
         return redirect('/listar')
     return render(request, 'lambda_app/partial/deletar_registro.html', {'aluno': aluno})

def pesquisa_aluno(request):
    nome_p = request.GET.get('nome_pesquisado', '')
    if nome_p != '' :
        alunos = Aluno.objects.filter(nome__icontains=nome_p)
        return render(request, 'lambda_app/partial/pesquisa_aluno.html', {'alunos': alunos})
    else:
        return redirect('/listar')

def pesquisa_cpf(request):
    cpf_p = request.GET.get('CPF_pesquisado', '')
    if cpf_p != '' :
        alunos = Aluno.objects.filter(cpf__icontains=cpf_p)
        return render(request, 'lambda_app/partial/pesquisa_cpf.html', {'alunos': alunos})
    else:
        return redirect('/listar')
