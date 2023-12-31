from django.db import models
from cuenta.models import Empleador, Trabajador

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


class Contrato(models.Model):
    id = models.AutoField(primary_key= True)
    restricciones = models.CharField(blank= False, max_length=500)
    tipo = models.CharField(blank= False, max_length=500)
    servicio = models.CharField(blank= False, max_length=500)
    duracion = models.CharField(blank= False, max_length=500)
    condiciones = models.CharField(blank= False, max_length=500)
    pago = models.FloatField(blank= False)
    fecha_inicio = models.DateField(blank=False)
    empleador_id = models.ForeignKey(Empleador, on_delete=models.CASCADE,blank=False)
    trabajador_id = models.ForeignKey(Trabajador, on_delete=models.CASCADE,blank=False)
    