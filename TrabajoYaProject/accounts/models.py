from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from datetime import date
# Create your models here.

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    es_empleador = models.BooleanField(default=False)
    es_trabajador = models.BooleanField(default=False)

def validar_numero(value):
    if not value.isdigit():
        raise ValidationError('This field must be numeric.')
    
def validar_edad(value):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 18:
        raise ValidationError("You must be at least 18 years old.")

class Empleador(models.Model): 
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True, related_name='empleador')
    foto= models.ImageField(upload_to='images/', null=True, blank=True)
    identificacion = models.CharField(max_length=10, validators=[validar_numero])
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(validators=[validar_edad])
    celular = models.CharField(max_length=50, validators=[validar_numero])
    
    def __str__(self):
        return self.name
    
class Trabajador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True, related_name='trabajador')
    foto= models.ImageField(upload_to='images/', null=True, blank=True)
    identificacion = models.CharField(max_length=10, validators=[validar_numero])
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(validators=[validar_edad])
    celular = models.CharField(max_length=50, validators=[validar_numero])
    habilidades= models.CharField(max_length=50)
    experiencia= models.CharField(max_length=50)
    calificacion_promedio= models.DecimalField(max_digits=3, decimal_places=2, default=0.0)

    def __str__(self):
        return self.nombre