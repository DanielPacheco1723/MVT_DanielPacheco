from django.db import models

# Create your models here.

class Familiares (models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    ult_edic = models.DateField()

class Datos (models.Model):

    telefono = models.CharField(max_length=40)
    edad = models.IntegerField()


