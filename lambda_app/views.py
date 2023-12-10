from django.shortcuts import render, get_object_or_404, redirect
from lambda_app.models import Aluno 
from lambda_app.forms import AlunoForm 
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
           return redirect('listar')
   else:
       form = AlunoForm()
   return render(request, 'lambda_app/partial/formulario_registro.html', {'form': form})

def atualizar_registro(request, pk):
   aluno = get_object_or_404(Aluno, pk=pk)
   if request.method == 'POST':
       form = AlunoForm(request.POST, instance=aluno)
       if form.is_valid():
           form.save()
           return redirect('listar')
   else:
       form = AlunoForm(instance=aluno)
   return render(request, 'lambda_app/partial/formulario_registro.html', {'form': form})

def deletar_registro(request, pk):
   aluno = get_object_or_404(Aluno, pk=pk)
   if request.method == 'POST':
       aluno.delete()
       return redirect('listar')
   return render(request, 'lambda_app/partial/deletar_registro.html', {'aluno': aluno})

