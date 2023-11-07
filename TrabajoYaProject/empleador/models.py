from django.db import models
from accounts.models import Empleador

# Create your models here.

class VacanteLaboral(models.Model):
    nombre = models.CharField(blank= False, max_length=200)
    tiempo = models.CharField(blank= False, max_length=200)
    ubicacion = models.CharField(blank= False, max_length=200)
    descripcion = models.TextField(blank= False, max_length=500)
    responsabilidades = models.TextField(blank= False, max_length=500)
    requisitos = models.TextField(blank= False, max_length=500)
    beneficios = models.TextField(blank= False, max_length=500)
    oferta = models.CharField(blank= False, max_length=200)
    empleador = models.ForeignKey(Empleador, on_delete=models.CASCADE,null=True, blank=True)
    disponibilidad = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name