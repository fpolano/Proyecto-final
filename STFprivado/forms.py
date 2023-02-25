from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class UsuarioFormulario(UserCreationForm):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['nombre', 'apellido', 'email', 'password1', 'password2'] 

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