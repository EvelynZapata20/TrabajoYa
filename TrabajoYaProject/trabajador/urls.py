from django.contrib import admin
from django.urls import path, include
from trabajador import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('trabajadores/', views.trabajadores, name='trabajadores'),
    path('perfil/<int:trabajador_id>/', views.perfil, name='perfil'),
]