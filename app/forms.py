from django import forms
from .models import *

#Creamos el formulario de Agregar un Programa
class ProgramaForm(forms.ModelForm):

    class Meta:
        model = Programa
        fields = ['nombre','conductor','certificadoLoc','imagen']

class ProgramacionForm(forms.ModelForm):

    class Meta:
        model = Programacion
        fields = '__all__'

class ArtistaForm(forms.ModelForm):

    class Meta:
        model = Artista
        fields = '__all__'

class PublicidadForm(forms.ModelForm):

    class Meta:
        model = Publicidad
        fields = '__all__'

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'