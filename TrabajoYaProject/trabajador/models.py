from django.db import models
from accounts.models import Trabajador as Trabajador_

# Create your models here.
class Trabajador(models.Model):
    identificacion= models.IntegerField(primary_key=True)
    foto= models.ImageField(upload_to='images/', null=True, blank=True)
    nombre= models.CharField(max_length=20)
    apellidos= models.CharField(max_length=30)
    correo_electronico= models.CharField(max_length=50)
    celular= models.IntegerField()
    fecha_nacimiento= models.DateField()
    contraseña= models.CharField(max_length=20)
    estado= models.BooleanField(default=True)
    biografia = models.TextField()
    certificaciones = models.TextField(null=True, blank=True)
    habilidades = models.TextField()
    experiencia_laboral = models.TextField()
    historial_contratacion= models.TextField(null=True, blank=True)


class ofertaServicio(models.Model):
    servicio = models.CharField(blank= False, max_length=200)
    disponibilidad = models.CharField(blank= False, max_length=200)
    restricciones = models.TextField(blank= False, max_length=500)
    lugar = models.TextField(blank= False, max_length=80)
    contacto = models.TextField(blank= False, max_length=30)
    precio = models.CharField(blank= False, max_length=30)
    trabajador = models.ForeignKey(Trabajador_, on_delete=models.CASCADE,null=True, blank=True)
    sigue = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    