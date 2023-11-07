from django.shortcuts import render, redirect, get_object_or_404
from pathlib import Path
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from trabajador.models import Trabajador
from .models import *
from .forms import *
from empleador.models import *
from empleador.forms import *


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

def verOfertas(request):
    terminoBusqueda = request.GET.get('terminoBusqueda')
    filtro = request.GET.get('filtroBusqueda')
    ofertas = ofertaServicio.objects.filter(trabajador=request.user.trabajador)
    if terminoBusqueda:
        if filtro == 'todo':
            ofertas = ofertas.filter(
                Q(servicio__icontains=terminoBusqueda) | 
                Q(disponibilidad__icontains=terminoBusqueda) |
                Q(restricciones__icontains=terminoBusqueda) | 
                Q(lugar__icontains=terminoBusqueda) | 
                Q(contacto__icontains=terminoBusqueda) | 
                Q(precio__icontains=terminoBusqueda)
            )
        elif filtro == 'servicio':
            ofertas = ofertas.filter(servicio__icontains=terminoBusqueda)
        elif filtro == 'disponibilidad':
            ofertas = ofertas.filter(disponibilidad__icontains=terminoBusqueda)
        elif filtro == 'lugar':
            ofertas = ofertas.filter(lugar__icontains=terminoBusqueda)
        elif filtro == 'precio':
            ofertas = ofertas.filter(precio__icontains=terminoBusqueda)

    return render(request, 'ofertasTrabajador.html', {'ofertas': ofertas})

def crearOferta(request):
    if request.method == 'POST':
        formulario = FormularioOferta(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.instance.trabajador = request.user.trabajador
            formulario.save()
            return redirect('verOfertas')
    else:
        formulario = FormularioOferta()
    return render(request, 'nuevaOferta.html', {'formulario': formulario})

def administrarOferta(request, ofertaID):
    oferta = get_object_or_404(ofertaServicio, pk=ofertaID)
    if request.method == 'POST':
        formulario = FormularioOferta(request.POST, request.FILES, instance=oferta)
        if formulario.is_valid():
            formulario.save()
            return redirect('administrarOferta', ofertaID=oferta.id)
    else:
        formulario = FormularioOferta(instance=oferta)
    return render(request, 'administrarOferta.html', {'oferta': oferta, 'formulario': formulario})

def eliminarOferta(request, ofertaID):
    oferta = get_object_or_404(ofertaServicio, pk=ofertaID)
    if request.method == 'POST':
        oferta.delete()
        return redirect('verOfertas')
    return render(request, 'administrarOferta.html', {'oferta': oferta})

def verVacantesTrabajador(request):
    vacantes = VacanteLaboral.objects.all()
    terminoBusqueda = request.GET.get('terminoBusqueda')
    filtro = request.GET.get('filtroBusqueda')
    if terminoBusqueda:
        if filtro == 'todo':
            vacantes = vacantes.filter(
                Q(nombre__icontains=terminoBusqueda) | 
                Q(tiempo__icontains=terminoBusqueda) |
                Q(ubicacion__icontains=terminoBusqueda) | 
                Q(descripcion__icontains=terminoBusqueda) | 
                Q(beneficios__icontains=terminoBusqueda) | 
                Q(empleador__nombre__icontains=terminoBusqueda)
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
        elif filtro == 'empleador':
            vacantes = vacantes.filter(empleador__nombre__icontains=terminoBusqueda)
    return render(request, 'vacantesTrabajador.html', {'vacantes': vacantes})

def masInfoVacante(request,vacanteID):
    vacante = get_object_or_404(VacanteLaboral, pk=vacanteID)
    return render(request, 'masInfoVacante.html', {'vacante': vacante})