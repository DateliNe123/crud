# advocacia/forms.py

from django import forms
from .models import Cliente, Processo

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone']

class ProcessoForm(forms.ModelForm):
    class Meta:
        model = Processo
        fields = ['cliente', 'nome', 'numero', 'data_abertura']