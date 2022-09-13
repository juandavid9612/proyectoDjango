from django.db import models

# Create your models here.

class Empleados(models.Model):
    nombre = models.CharField( max_length=50)
    apellido = models.CharField( max_length=50)
    tipoDocumento = models.CharField(max_length=25)
    numeroDocumento = models.IntegerField()
    correo = models.EmailField(max_length=254)
    telefono = models.IntegerField()
    tipoSangre = models.CharField( max_length=25)