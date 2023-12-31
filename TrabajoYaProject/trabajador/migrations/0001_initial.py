# Generated by Django 3.2.8 on 2023-11-17 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cuenta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('identificacion', models.IntegerField(primary_key=True, serialize=False)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('nombre', models.CharField(max_length=20)),
                ('apellidos', models.CharField(max_length=30)),
                ('correo_electronico', models.CharField(max_length=50)),
                ('celular', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('contraseña', models.CharField(max_length=20)),
                ('estado', models.BooleanField(default=True)),
                ('biografia', models.TextField()),
                ('certificaciones', models.TextField(blank=True, null=True)),
                ('habilidades', models.TextField()),
                ('experiencia_laboral', models.TextField()),
                ('historial_contratacion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ofertaServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicio', models.CharField(max_length=200)),
                ('disponibilidad', models.CharField(max_length=200)),
                ('restricciones', models.TextField(max_length=500)),
                ('lugar', models.TextField(max_length=80)),
                ('contacto', models.TextField(max_length=30)),
                ('precio', models.CharField(max_length=30)),
                ('sigue', models.BooleanField(default=False)),
                ('trabajador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cuenta.trabajador')),
            ],
        ),
    ]
