from django.db.models import Q
from pathlib import Path
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import *
import re
from .models import *
from accounts.models import *
from accounts.forms import *
from trabajador.forms import *
from trabajador.models import *


# Create your views here.


def verVacantes(request):
    vacantes = VacanteLaboral.objects.filter(empleador=request.user.empleador)
    terminoBusqueda = request.GET.get('terminoBusqueda')
    filtro = request.GET.get('filtroBusqueda')
    if terminoBusqueda:
        if filtro == 'todo':
            vacantes = vacantes.filter(
                Q(nombre__icontains=terminoBusqueda) | 
                Q(tiempo__icontains=terminoBusqueda) |
                Q(ubicacion__icontains=terminoBusqueda) | 
                Q(descripcion__icontains=terminoBusqueda) | 
                Q(beneficios__icontains=terminoBusqueda)
            )
        elif filtro == 'nombre':
            vacantes = vacantes.filter(nombre__icontains=terminoBusqueda)
        elif filtro == 'tiempo':
            vacantes = vacantes.filter(tiempo__icontains=terminoBusqueda)
        elif filtro == 'ubicacion':
            vacantes = vacantes.filter(ubicacion__icontains=terminoBusqueda)
        elif filtro == 'descripcion':
            vacantes = vacantes.filter(descripcion__icontains=terminoBusqueda)
        elif filtro == 'beneficios':
            vacantes = vacantes.filter(beneficios__icontains=terminoBusqueda)

    return render(request, 'vacantesEmpleador.html', {'vacantes': vacantes})


def crearVacante(request):
    if request.method == 'POST':
        formulario = FormularioVacante(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.instance.empleador = request.user.empleador
            formulario.save()
            return redirect('verVacantes')
    else:
        formulario = FormularioVacante()
    return render(request, 'nuevaVacante.html', {'formulario': formulario})

def administrarVacante(request, vacanteID):
    vacante = get_object_or_404(VacanteLaboral, pk=vacanteID)
    if request.method == 'POST':
        formulario = FormularioVacante(request.POST, request.FILES, instance=vacante)
        if formulario.is_valid():
            formulario.save()
            return redirect('administrarVacante', vacanteID=vacante.id)
    else:
        formulario = FormularioVacante(instance=vacante)
    return render(request, 'administrarVacante.html', {'vacante': vacante, 'formulario': formulario})

def eliminarVacante(request, vacanteID):
    vacante = get_object_or_404(VacanteLaboral, pk=vacanteID)
    if request.method == 'POST':
        vacante.delete()
        return redirect('verVacantes')
    return render(request, 'administrarVacante.html', {'vacante': vacante})

def verOfertasEmpleador(request):
    ofertas = ofertaServicio.objects.all()
    terminoBusqueda = request.GET.get('terminoBusqueda')
    filtro = request.GET.get('filtroBusqueda')
    if terminoBusqueda:
        if filtro == 'todo':
            ofertas = ofertas.filter(
                Q(servicio__icontains=terminoBusqueda) | 
                Q(disponibilidad__icontains=terminoBusqueda) |
                Q(restricciones__icontains=terminoBusqueda) | 
                Q(lugar__icontains=terminoBusqueda) | 
                Q(contacto__icontains=terminoBusqueda) | 
                Q(precio__icontains=terminoBusqueda) |
                Q(trabajador__nombre__icontains=terminoBusqueda)
            )
        elif filtro == 'servicio':
            ofertas = ofertas.filter(servicio__icontains=terminoBusqueda)
        elif filtro == 'disponibilidad':
            ofertas = ofertas.filter(disponibilidad__icontains=terminoBusqueda)
        elif filtro == 'lugar':
            ofertas = ofertas.filter(lugar__icontains=terminoBusqueda)
        elif filtro == 'precio':
            ofertas = ofertas.filter(precio__icontains=terminoBusqueda)
        elif filtro == 'trabajador':
            ofertas = ofertas.filter(trabajador__nombre__icontains=terminoBusqueda)
    return render(request, 'ofertasEmpleador.html', {'ofertas': ofertas})

def masInfoOferta(request,ofertaID):
    oferta = get_object_or_404(ofertaServicio, pk=ofertaID)
    return render(request, 'masInfoOferta.html', {'oferta': oferta})