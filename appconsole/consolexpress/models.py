from django.db import models

# Create your models here.

class consola(models.Model):
    codigo = models.CharField(max_length=10)
    imagen = models.ImageField(upload_to='consolexpress/')
    nombre = models.CharField(max_length=75)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=75)
    marca = models.CharField(max_length=75)
    precio = models.CharField(max_length=75)
    stock = models.IntegerField()