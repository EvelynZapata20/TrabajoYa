# Generated by Django 4.2.4 on 2023-11-22 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0003_auto_20231120_2223'),
        ('empleador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('restricciones', models.CharField(max_length=500)),
                ('tipo', models.CharField(max_length=500)),
                ('servicio', models.CharField(max_length=500)),
                ('duracion', models.CharField(max_length=500)),
                ('condiciones', models.CharField(max_length=500)),
                ('pago', models.FloatField()),
                ('fecha_inicio', models.DateField()),
                ('empleador_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuenta.empleador')),
                ('trabajador_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuenta.trabajador')),
            ],
        ),
    ]
