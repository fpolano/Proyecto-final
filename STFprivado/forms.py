from django import forms
from .models import *

class OrdenesFormulario(forms.ModelForm):
    class Meta:
        model = Ordenes
        fields = ['estado', 'cliente', 'tipo', 'marca', 'modelo', 'obs', 'presupuesto']
        labels = {'obs':'Observaciones'}

class ClientesFormulario(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['razonSocial', 'cuit', 'contacto', 'email', 'telefono', 'direccion']
        labels = {'razonSocial':'Razón Social','email':'Correo electrónico'}