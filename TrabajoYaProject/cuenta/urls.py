from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login_view.as_view(), name='login'),
    path('empleador_signup/', views.empleador_signup.as_view(), name='empleador_signup'),
    path('trabajador_signup/', views.trabajador_signup.as_view(), name='trabajador_signup'),
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('configuracion_empleador/', views.configuracion_empleador, name='configuracion_empleador'),
    path('configuracion_trabajador/', views.configuracion_trabajador, name='configuracion_trabajador'),
]