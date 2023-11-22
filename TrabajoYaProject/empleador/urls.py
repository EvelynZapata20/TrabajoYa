from django.contrib import admin
from django.urls import path, include
from empleador import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('misVacantes/', views.verVacantes, name='verVacantes'),
    path('nuevaVacante/', views.crearVacante, name='crearVacante'),
    path('administrarVacante/<int:vacanteID>', views.administrarVacante, name='administrarVacante'),
    path('eliminarVacante/<int:vacanteID>/', views.eliminarVacante, name='eliminarVacante'),
    path('verOfertasEmpleador/', views.verOfertasEmpleador, name='verOfertasEmpleador'),
    path('masInfo/<int:ofertaID>/', views.masInfoOferta, name='masInfo'),
    path('contrato/', views.contrato, name='contrato'),
]