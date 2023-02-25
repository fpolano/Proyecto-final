from django.db import models

# Create your models here.
#################### Base de datos Máquinas ####################
class Maquinas(models.Model):
    nombre = models.CharField(max_length=60)
    tipo = models.CharField(max_length=60)
    marca = models.CharField(max_length=60)
    modelo = models.CharField(max_length=60)
    desc = models.TextField(max_length=400)
    precio = models.FloatField()
    stock = models.SmallIntegerField()
    foto = models.ImageField(upload_to='maquinas', null = True, blank = True)
    # foto = models.ImageField(upload_to='maquinas', null = True, blank = True, default='settings.MEDIA_ROOT/maquinas/amola.jpg')
    
    def __str__(self):
        return f"{self.nombre} Marca:{self.marca} Modelo:{self.modelo} precio: ${self.precio}"

#################### Base de datos respuestos a la venta ####################
class Repuestos(models.Model):
    nombre = models.CharField(max_length=60)
    marca = models.CharField(max_length=60)
    modelo = models.CharField(max_length=60)
    precio = models.FloatField()
    stock = models.SmallIntegerField()
    foto = models.ImageField(upload_to='repuestos', null = True, blank = True)
    #foto = models.ImageField(upload_to='repuestos', null = True, blank = True, default='settings.MEDIA_ROOT/repuestos/llave.jpg')
    
    def __str__(self):
        return f"{self.nombre} Marca:{self.marca} Modelo:{self.modelo} Precio: ${self.precio}"    

#################### Base de datos de manuales ####################
class Manuales(models.Model):
    tipo = models.CharField(max_length=60)
    marca = models.CharField(max_length=60)
    modelo = models.CharField(max_length=60)
    archivo = models.FileField(upload_to='manuales', null = True, blank = True)

    def __str__(self):
        return f"Manual de {self.tipo} Marca:{self.marca} Modelo:{self.modelo}"   