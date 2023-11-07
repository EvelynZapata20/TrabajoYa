from django import forms
from .models import *

class FormularioOferta(forms.ModelForm):
    class Meta:
        model= ofertaServicio
        fields= ['servicio', 'disponibilidad', 'restricciones', 'lugar', 'contacto', 'precio', 'sigue']
        widgets = {
            'sigue': forms.CheckboxInput(attrs={'class': 'check-box'}),
        }