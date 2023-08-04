from django.db import models

# Create your models here.

class Coberturas(models.Model):
    nombre = models.CharField(max_length=40)
    ramo = models.CharField(max_length=40)
    #def __str__(self):
       # return f"Nombre: {self.nombre} - Ramo {self.ramo}"

class Aseguradoras(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.IntegerField()
    #def __str__(self):
     #   return f"Nombre: {self.nombre} - Direccion {self.direccion} - E-Mail {self.email} - Telefono {self.telefono}"

class Productores(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.IntegerField()