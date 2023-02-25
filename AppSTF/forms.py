from django import forms
from .models import *

class MaquinasFormulario(forms.ModelForm):
    class Meta:
        model = Maquinas
        fields = ['nombre', 'tipo', 'marca', 'modelo', 'desc', 'precio', 'stock', 'foto']
        labels = {'desc':'Descripción','foto':'Imagen'}

class RepuestosFormulario(forms.ModelForm):
    class Meta:
        model = Repuestos
        fields = ['nombre', 'marca', 'modelo', 'precio', 'stock','foto']
        labels = {'foto':'Imagen'}

class ManualesFormulario(forms.ModelForm):
    class Meta:
        model = Manuales
        fields = ['tipo', 'marca', 'modelo','archivo']
