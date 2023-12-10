from django import forms
from .models import Aluno 

class AlunoForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput())
    cpf = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput())
    telefone = forms.CharField(widget=forms.TextInput())
    matriculado = forms.BooleanField(widget=forms.CheckboxInput())
    class Meta:
       model = Aluno 
       fields = ['nome', 'cpf', 'email', 'telefone', 'matriculado']
