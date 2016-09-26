from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Reclamo(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.IntegerField()
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    descripcion = models.TextField()

    def __str__(self):
        return "(" + self.nombre + " " + self.apellido + ") " + self.descripcion
