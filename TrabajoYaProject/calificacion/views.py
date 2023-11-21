from django.shortcuts import render, redirect
from cuenta.models import Empleador
from trabajador.models import ofertaServicio
from .models import Calificacion
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def calificar_oferta_servicio(request, oferta_servicio_id):
    oferta_servicio = ofertaServicio.objects.get(pk=oferta_servicio_id)
    empleador = Empleador.objects.get(usuario=request.user.empleador)

    calificado = Calificacion.objects.filter(empleador=empleador, oferta_servicio=oferta_servicio).exists()
    promedio = None

    if request.method == 'POST' and not calificado:
        calidad_servicio = int(request.POST['calidad_servicio'])
        puntualidad = int(request.POST['puntualidad'])
        profesionalismo = int(request.POST['profesionalismo'])
        cumplimiento_acuerdos = int(request.POST['cumplimiento_acuerdos'])
        trato_personal = int(request.POST['trato_personal'])
        eficiencia = int(request.POST['eficiencia'])
        
        Calificacion.objects.create(
            oferta_servicio=oferta_servicio,
            empleador=empleador,
            calidad_servicio=calidad_servicio,
            puntualidad=puntualidad,
            profesionalismo=profesionalismo,
            cumplimiento_acuerdos=cumplimiento_acuerdos,
            trato_personal=trato_personal,
            eficiencia=eficiencia
        )
        return redirect('masInfo', ofertaID=oferta_servicio_id)

    elif calificado:
        # Calcular el promedio de los campos de calificación
        calificacion_existente = Calificacion.objects.get(empleador=empleador, oferta_servicio=oferta_servicio)
        promedio = (
            calificacion_existente.calidad_servicio +
            calificacion_existente.puntualidad +
            calificacion_existente.profesionalismo +
            calificacion_existente.cumplimiento_acuerdos +
            calificacion_existente.trato_personal +
            calificacion_existente.eficiencia
        ) / 6.0

    return render(request, 'calificar.html', {'oferta_servicio': oferta_servicio, 'calificado': calificado, 'promedio': promedio})