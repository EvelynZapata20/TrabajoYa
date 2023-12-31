from django.db import models
from cuenta.models import Empleador
from trabajador.models import ofertaServicio
from django.db import models
from django.db.models import Avg
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Calificacion(models.Model):
    empleador= models.ForeignKey(Empleador, on_delete=models.CASCADE)
    oferta_servicio = models.ForeignKey(ofertaServicio, on_delete=models.CASCADE)
    calidad_servicio = models.PositiveIntegerField()
    puntualidad= models.PositiveIntegerField()
    profesionalismo= models.PositiveIntegerField()
    cumplimiento_acuerdos= models.PositiveIntegerField()
    trato_personal= models.PositiveIntegerField()
    eficiencia= models.PositiveIntegerField()

@receiver(post_save, sender=Calificacion)
def actualizar_promedio(sender, instance, **kwargs):
    oferta_servicio = instance.oferta_servicio
    promedio_calificaciones = Calificacion.objects.filter(oferta_servicio=oferta_servicio).aggregate(
        Avg('calidad_servicio'),
        Avg('puntualidad'),
        Avg('profesionalismo'),
        Avg('cumplimiento_acuerdos'),
        Avg('trato_personal'),
        Avg('eficiencia')
    )

    promedio_general = sum(promedio_calificaciones.values()) / 6
    oferta_servicio.calificacion_promedio = promedio_general
    oferta_servicio.save()