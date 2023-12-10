from django import forms
from .models import Aluno 

class AlunForm(forms.ModelForm):
   class Meta:
       model = Aluno 
       fields = ['nome', 'cpf', 'email', 'telefone', 'matriculado']
