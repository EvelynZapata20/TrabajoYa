from django.shortcuts import render, redirect
from .models import prestacionSocial
import random

def verPrestaciones(request):
    prestaciones = prestacionSocial.objects.all()
    return render(request, 'verPrestaciones.html', {'prestaciones': prestaciones})

def redirigirSitioOficial(request, pk):
    prestacion = prestacionSocial.objects.get(pk=pk)
    return redirect(prestacion.sitio_oficial)
