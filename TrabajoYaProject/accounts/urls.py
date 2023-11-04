from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login_view.as_view(), name='login'),
    path('empleador_signup/', views.empleador_signup.as_view(), name='empleador_signup'),
    path('trabajador_signup/', views.trabajador_signup.as_view(), name='trabajador_signup'),
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
]