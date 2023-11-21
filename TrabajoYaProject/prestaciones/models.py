from django.db import models

class prestacionSocial(models.Model):
    nombre= models.CharField(max_length=100)
    entidad = models.CharField(max_length=100)
    periodicidad = models.CharField(max_length=50)
    beneficios = models.TextField()
    requisitos = models.TextField()
    sitio_oficial = models.URLField()

    def __str__(self):
        return self.nombre