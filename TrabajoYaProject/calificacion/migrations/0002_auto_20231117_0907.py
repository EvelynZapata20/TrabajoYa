# Generated by Django 3.2.8 on 2023-11-17 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trabajador', '0003_ofertaservicio_calificacion_promedio'),
        ('calificacion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calificacion',
            name='trabajador',
        ),
        migrations.AddField(
            model_name='calificacion',
            name='oferta_servicio',
            field=models.ForeignKey(default=0.0, on_delete=django.db.models.deletion.CASCADE, to='trabajador.ofertaservicio'),
            preserve_default=False,
        ),
    ]
