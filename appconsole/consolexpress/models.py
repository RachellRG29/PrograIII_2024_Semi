from django.db import models

#BASE DE DATOS - bd_consolexpress
# Tabla consolas 
class consola(models.Model):
    codigo = models.CharField(max_length=10)
    imagen = models.ImageField(upload_to='img_consolas/')
    nombre = models.CharField(max_length=75)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=75)
    marca = models.CharField(max_length=75)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre