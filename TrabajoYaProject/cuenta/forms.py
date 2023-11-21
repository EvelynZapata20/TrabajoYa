from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from .models import Usuario, Empleador, Trabajador, validar_edad, validar_numero
from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class empleador_form_registro(UserCreationForm):
    # fields for user
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    foto= forms.ImageField()
    identificacion = forms.CharField(widget=forms.TextInput(), validators=[validar_numero])
    nombre = forms.CharField(widget=forms.TextInput())
    apellidos= forms.CharField(widget=forms.TextInput())
    fecha_nacimiento = forms.DateField(validators=[validar_edad])
    celular = forms.CharField(widget=forms.TextInput(), validators=[validar_numero])

    # allows the form to inherit metadata from the base in Django form for user registration.
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')

    # ensures that all the database operations within this method are treated as a single unit
    @transaction.atomic
    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.es_empleador = True
        if commit:
            usuario.save()
        empleador = Empleador.objects.create(usuario=usuario, foto=self.cleaned_data.get('foto'), identificacion=self.cleaned_data.get('identificacion'), nombre=self.cleaned_data.get('nombre'), apellidos= self.cleaned_data.get('apellidos'), fecha_nacimiento=self.cleaned_data.get('fecha_nacimiento'), celular=self.cleaned_data.get('celular'))
        return usuario


class trabajador_form_registro(UserCreationForm):
    # fields for user
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    foto= forms.ImageField()
    identificacion = forms.CharField(widget=forms.TextInput(), validators=[validar_numero])
    nombre = forms.CharField(widget=forms.TextInput())
    apellidos= forms.CharField(widget=forms.TextInput())
    fecha_nacimiento = forms.DateField(validators=[validar_edad])
    celular = forms.CharField(widget=forms.TextInput(), validators=[validar_numero])
    habilidades= forms.CharField(widget=forms.TextInput())
    experiencia= forms.CharField(widget=forms.TextInput())

    # allows the form to inherit metadata from the base in Django form for user registration.
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')
    
    # ensures that all the database operations within this method are treated as a single unit
    @transaction.atomic
    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.es_trabajador = True
        if commit:
            usuario.save()
        trabajador = Trabajador.objects.create(usuario=usuario, foto=self.cleaned_data.get('foto'), identificacion=self.cleaned_data.get('identificacion'), nombre=self.cleaned_data.get('nombre'), apellidos= self.cleaned_data.get('apellidos'), fecha_nacimiento=self.cleaned_data.get('fecha_nacimiento'), celular=self.cleaned_data.get('celular'), habilidades= self.cleaned_data.get('habilidades'), experiencia= self.cleaned_data.get('experiencia'))
        return usuario

# form for the login
class login_form(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class trabajador_actualizar(forms.ModelForm):
    class Meta:
        model= Trabajador
        fields= ['foto', 'identificacion', 'nombre', 'apellidos', 'fecha_nacimiento', 'celular', 'habilidades', 'experiencia']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }


class empleador_actualizar(forms.ModelForm):
    class Meta:
        model= Empleador
        fields= ['foto', 'identificacion', 'nombre', 'apellidos', 'fecha_nacimiento', 'celular']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }