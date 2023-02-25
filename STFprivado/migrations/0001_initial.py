# Generated by Django 4.1.6 on 2023-02-24 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razonSocial', models.CharField(max_length=60)),
                ('cuit', models.PositiveSmallIntegerField(blank=True)),
                ('contacto', models.CharField(blank=True, max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.PositiveSmallIntegerField()),
                ('direccion', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ordenes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('IN', 'Ingresado'), ('RE', 'Revisado'), ('PR', 'PResupuestado'), ('AC', 'Aceptado'), ('NC', 'Rechazado'), ('RP', 'Reparado'), ('RT', 'Retirado')], default='IN', max_length=2)),
                ('fechaIngreso', models.DateField(auto_now_add=True)),
                ('cliente', models.CharField(max_length=60)),
                ('tipo', models.CharField(max_length=60)),
                ('marca', models.CharField(max_length=60)),
                ('modelo', models.CharField(max_length=60)),
                ('obs', models.TextField(max_length=300)),
                ('presupuesto', models.FloatField(blank=True)),
            ],
        ),
    ]
