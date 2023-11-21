from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('calificar_oferta_servicio/<int:oferta_servicio_id>/', views.calificar_oferta_servicio, name='calificar_oferta_servicio'),
]