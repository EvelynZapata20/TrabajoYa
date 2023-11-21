from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import PasswordChangeForm, PasswordChangeForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import update_session_auth_hash, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from cuenta.models import Usuario, Empleador, Trabajador
from cuenta.forms import empleador_form_registro, trabajador_form_registro, login_form, trabajador_actualizar, empleador_actualizar
from empleador.urls import *
from django.http import HttpResponseRedirect
# View for the home page
def home(request):
    return render(request, 'home.html')
    

class empleador_signup(CreateView):
    model = Usuario
    form_class = empleador_form_registro
    template_name = 'empleador_signup.html'

    # Add aditional data to the template
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'empleador'
        return super().get_context_data(**kwargs)

    # Save the data in the database
    def form_valid(self, form):
        usuario = form.save()
        login(self.request, usuario)
        return redirect('verVacantes')
    

class trabajador_signup(CreateView):
    model = Usuario
    form_class = trabajador_form_registro
    template_name = 'trabajador_signup.html'

    # Add aditional data to the template
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'trabajador'
        return super().get_context_data(**kwargs)

    # Save the data in the database
    def form_valid(self, form):
        usuario = form.save()
        login(self.request, usuario)
        return redirect('trabajadores')
    
# View for the login
class login_view(LoginView):
    template_name = 'login.html'

    # Ensures the data from the parent class is preserved
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    # Ensures that the user is redirected to the correct page
    def get_success_url(self):
        usuario= self.request.user
        if usuario.is_authenticated:
            # Redirect to the correct page depending on the user type
            if usuario.es_empleador:
                return reverse('verVacantes')
            elif usuario.es_trabajador:
                return reverse('trabajadores')
        else:
            return reverse('login')
        


@login_required
def configuracion_trabajador(request):
    trabajador = Trabajador.objects.get(usuario=request.user)
    form = trabajador_actualizar(instance=trabajador)
    form2 = PasswordChangeForm(request.user)

    if request.method == 'POST':
        if 'update_account' in request.POST:
            form = trabajador_actualizar(request.POST, instance=trabajador)
            if form.is_valid():
                form.save()
                return redirect('configuracion_trabajador') 
            
        # Verify if the submmited form is the change password form
        elif 'change_password' in request.POST:
            form2 = PasswordChangeForm(request.user, request.POST)
            if form2.is_valid():
                usuario = form2.save()
                messages.success(request, 'Tu contraseña ha cambiado exitosamente!')
                return redirect('/cuenta/login/?next=/cuenta/configuracion_trabajador/')

    return render(request, 'configuracion_trabajador.html', {'form': form, 'form2': form2})


@login_required
def configuracion_empleador(request):
    empleador = Empleador.objects.get(usuario=request.user)
    form = empleador_actualizar(instance=empleador)
    form2 = PasswordChangeForm(request.user)

    if request.method == 'POST':
        if 'update_account' in request.POST:
            form = empleador_actualizar(request.POST, instance=empleador)
            if form.is_valid():
                form.save()
                return redirect('configuracion_empleador') 
            
        # Verify if the submitted form is the change password form
        elif 'change_password' in request.POST:
            form2 = PasswordChangeForm(request.user, request.POST)
            if form2.is_valid():
                usuario = form2.save()
                return redirect('/cuenta/login/?next=/cuenta/configuracion_empleador/')

    return render(request, 'configuracion_empleador.html', {'form': form, 'form2': form2})