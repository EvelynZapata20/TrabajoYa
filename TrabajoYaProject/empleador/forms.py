from django import forms
from .models import *

class FormularioVacante(forms.ModelForm):
    class Meta:
        model= VacanteLaboral
        fields= ['nombre', 'tiempo', 'ubicacion', 'descripcion', 'responsabilidades', 'requisitos', 'beneficios', 'oferta', 'disponibilidad']
        widgets = {
            'disponibilidad': forms.CheckboxInput(attrs={'class': 'check-box'}),
        }