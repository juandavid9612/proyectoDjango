from django.db import models

# Create your models here.

#(Ano, Mes, Estudio, Institución, Titulo obtenido), 
class Estudios(models.Model):
    ano = models.IntegerField()
    mes = models.IntegerField()    
    estudio = models.CharField( max_length=50)
    institucion = models.CharField( max_length=50)
    tituloObtenido = models.CharField( max_length=50)

#(Ano, Mes, Empresa, Jefe inmediato, Cargo, Responsabilidades, Logros realizados)
class Experiencias(models.Model):
    ano = models.IntegerField()
    mes = models.IntegerField()  
    empresa = models.CharField( max_length=50)
    jefeInmediato = models.CharField( max_length=50)
    cargo = models.CharField( max_length=50)
    responsabilidades = models.CharField( max_length=50)
    logrosRealizados = models.CharField( max_length=50)

#(Nombre, Apellido, Tipo de documento, numero de documento, correo, teléfono, tipo de sangre), 
class Empleados(models.Model):
    nombre = models.CharField( max_length=50)
    apellido = models.CharField( max_length=50)
    tipoDocumento = models.CharField(max_length=25)
    numeroDocumento = models.FloatField()
    correo = models.EmailField(max_length=254)
    telefono = models.IntegerField()
    tipoSangre = models.CharField( max_length=25)
    idEstudios = models.ForeignKey(Estudios, on_delete=models.CASCADE,null=True, blank=True)
    idExperiencias = models.ForeignKey(Experiencias, on_delete=models.CASCADE,null=True, blank=True)
    