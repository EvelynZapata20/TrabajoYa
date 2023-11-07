from django.contrib import admin
from django.urls import path, include
from trabajador import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('trabajadores/', views.trabajadores, name='trabajadores'),
    path('perfil/<int:trabajador_id>/', views.perfil, name='perfil'),
    path('misOfertas/', views.verOfertas, name='verOfertas'),
    path('crearOferta/', views.crearOferta, name='crearOferta'),
    path('administrarOferta/<int:ofertaID>', views.administrarOferta, name='administrarOferta'),
    path('eliminarOferta/<int:ofertaID>/', views.eliminarOferta, name='eliminarOferta'),
    path('verVacantesTrabajador/', views.verVacantesTrabajador, name='verVacantesTrabajador'),
    path('masInfoVacante/<int:vacanteID>/', views.masInfoVacante, name='masInfoVacante'),
]