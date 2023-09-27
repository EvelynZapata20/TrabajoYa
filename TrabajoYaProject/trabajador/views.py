from django.shortcuts import render, redirect, get_object_or_404
from pathlib import Path
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from trabajador.models import Trabajador

# Create your views here.

def home(request):
    return HttpResponse('Hello, World!')

def trabajadores(request):
    buscar_termino = request.GET.get('buscarTermino')
    if buscar_termino:
        trabajadores = Trabajador.objects.filter(
                Q(nombre__icontains=buscar_termino) |  Q(apellidos__icontains=buscar_termino) | Q(celular__icontains=buscar_termino) |
                Q(habilidades__icontains=buscar_termino) | Q(experiencia_laboral__icontains=buscar_termino)
            )
    else:
        trabajadores= Trabajador.objects.all()
    return render(request, 'trabajadores.html', {'trabajadores': trabajadores})

def perfil(request, trabajador_id):
    trabajador = get_object_or_404(Trabajador, pk=trabajador_id)
    return render(request, 'perfil.html', {'trabajador': trabajador})