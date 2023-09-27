from django.db import models
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
