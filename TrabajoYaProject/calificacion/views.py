from django.shortcuts import render, redirect
from accounts.models import Trabajador, Empleador
from .models import Calificacion
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def calificar_trabajador(request, trabajador_id):
    if request.method == 'POST':
        trabajador = Trabajador.objects.get(pk=trabajador_id)
        empleador = Empleador.objects.get(usuario=request.user.empleador)
        calidad_servicio = request.POST['calidad_servicio']
        puntualidad = request.POST['puntualidad']
        profesionalismo = request.POST['profesionalismo']
        cumplimiento_acuerdos = request.POST['cumplimiento_acuerdos']
        trato_personal = request.POST['trato_personal']
        eficiencia = request.POST['eficiencia']
        
        Calificacion.objects.create(
            trabajador=trabajador,
            empleador=empleador,
            calidad_servicio=calidad_servicio,
            puntualidad=puntualidad,
            profesionalismo=profesionalismo,
            cumplimiento_acuerdos=cumplimiento_acuerdos,
            trato_personal=trato_personal,
            eficiencia=eficiencia
        )
        return HttpResponse('Trabajador Calificado') 
    
    trabajador = Trabajador.objects.get(pk=trabajador_id)
    return render(request, 'calificar.html', {'trabajador': trabajador})
