from django.db import models

# Create your models here.
#################### Base de datos ordenes de reparación ####################
class Ordenes(models.Model):
    opcionesEstado = [('IN','Ingresado'),
                      ('RE','Revisado'),
                      ('PR','Presupuestado'),
                      ('AC','Aceptado'),
                      ('NC','Rechazado'),
                      ('RP','Reparado'),
                      ('RT','Retirado'),
                      ]
    estado = models.CharField(max_length = 2,choices = opcionesEstado,default = 'IN')
    fechaIngreso = models.DateField(auto_now_add = True)
    cliente = models.CharField(max_length=60)
    tipo = models.CharField(max_length=60)
    marca = models.CharField(max_length=60)
    modelo = models.CharField(max_length=60)
    obs = models.TextField(max_length=300)
    presupuesto = models.FloatField(blank = True)
    
    def __str__(self):
        return f"Cliente: {self.cliente}; Máquina:{self.tipo};Fecha ingreso: {self.fechaIngreso}; Estado: {self.estado}"

#################### base de datos de clientes ####################
class Clientes(models.Model):
    razonSocial = models.CharField(max_length=60)
    cuit = models.PositiveSmallIntegerField(blank = True)
    contacto = models.CharField(max_length=60,blank=True)
    email = models.EmailField()
    telefono = models.PositiveSmallIntegerField()
    direccion = models.CharField(max_length=100,blank = True)
    
    def __str__(self):
        return f"{self.razonSocial} cuit: {self.cuit}"   