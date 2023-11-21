# urls.py
from django.urls import path
from .views import verPrestaciones

urlpatterns = [
    path('verPrestaciones/', verPrestaciones, name='verPrestaciones'),
]
