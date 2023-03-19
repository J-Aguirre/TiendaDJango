from django import forms

from .models import Departamento

class NewDepartamentoForm(forms.Form):
    nombre = forms.CharField(max_length=32)
    apellidos = forms.CharField(max_length=32)
    departamento = forms.CharField(max_length=32)
    short_name = forms.CharField(max_length=16)

