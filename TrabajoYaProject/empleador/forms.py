from django import forms
from .models import *

class FormularioVacante(forms.ModelForm):
    class Meta:
        model= VacanteLaboral
        fields= ['nombre', 'tiempo', 'ubicacion', 'descripcion', 'responsabilidades', 'requisitos', 'beneficios', 'oferta', 'disponibilidad']
        widgets = {
            'disponibilidad': forms.CheckboxInput(attrs={'class': 'check-box'}),
        }

class FormularioContrato(forms.ModelForm):
    class Meta:
        model= Contrato
        fields= ['restricciones', 'tipo', 'servicio', 'duracion','condiciones','pago','fecha_inicio']
        exclude = ['empleador_id','trabajador_id']
        widgets = {
            'restricciones': forms.Textarea(),
            'tipo': forms.Textarea(),
            'servicio': forms.Textarea(),
            'duracion': forms.Textarea(),
            'condiciones': forms.Textarea(),
            'pago': forms.Textarea(),
            'fecha_inicio': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'type': 'date', 'max': '2030-01-01', 'min': '2000-01-01'}),
        }