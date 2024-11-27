from django.db import models

#BASE DE DATOS - bd_consolexpress
# Tabla consolas 
class consola(models.Model):
    CATEGORIA_CHOICES = [
        ('consola', 'Consola'),
        ('especial', 'Especial'),
        ('accesorio', 'Accesorio'),
    ]

    PRESENTACION_CHOICES = [
        ('paquete_completo', 'Paquete completo'),
        ('individual', 'Individual'),
    ]

    codigo = models.CharField(max_length=10)
    imagen = models.ImageField(upload_to='img_consolas/')
    nombre = models.CharField(max_length=75)
    descripcion = models.TextField()
    presentacion = models.CharField(max_length=20, choices=PRESENTACION_CHOICES, default='individual' )
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    marca = models.CharField(max_length=75)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

def __str__(self):
    return self.nombre

#Tabla Tarjeta
class Tarjeta(models.Model):
    numero_tarjeta = models.CharField(max_length=16)
    titular = models.CharField(max_length=100)
    fecha_vencimiento = models.DateField()
    tipo_tarjeta = models.CharField(max_length=50)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    cvv = models.CharField(max_length=3)  # Este es el campo que necesitamos agregar correctamente

    def __str__(self):
        return f"{self.numero_tarjeta} - {self.titular}"