from django.shortcuts import render, get_object_or_404, redirect
from .models import Aluno 
from .forms import AlunForm 
# Create your views here.


def index(request):
    return render(request, "lambda_app/partial/principal.html")


def listar(request):
   alunos = Aluno.objects.all()
   return render(request, 'lambda_app/partial/listar_alunos.html', {'alunos': alunos})

def registrar_aluno(request):
   if request.method == 'POST':
       formulario = AlunoForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('listar')
   else:
       formulario = AlunoForm()
   return render(request, 'lambda_app/partial/formulario_registro.html', {'formulario': formulario})

def atualizar_registro(request, pk):
   aluno = get_object_or_404(Aluno, pk=pk)
   if request.method == 'POST':
       formulario = AlunoForm(request.POST, instance=aluno)
       if formulario.is_valid():
           formulario.save()
           return redirect('listar')
   else:
       form = AlunoForm(instance=aluno)
   return render(request, 'lambda_app/partial/formulario_registro.html', {'formulario': formulario})

def deletar_registro(request, pk):
   aluno = get_object_or_404(Aluno, pk=pk)
   if request.method == 'POST':
       aluno.delete()
       return redirect('listar')
   return render(request, 'lambda_app/partial/deletar_registro.html', {'aluno': aluno})

