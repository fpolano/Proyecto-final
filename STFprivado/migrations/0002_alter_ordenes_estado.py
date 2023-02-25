# Generated by Django 4.1.6 on 2023-02-25 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('STFprivado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenes',
            name='estado',
            field=models.CharField(choices=[('IN', 'Ingresado'), ('RE', 'Revisado'), ('PR', 'Presupuestado'), ('AC', 'Aceptado'), ('NC', 'Rechazado'), ('RP', 'Reparado'), ('RT', 'Retirado')], default='IN', max_length=2),
        ),
    ]
