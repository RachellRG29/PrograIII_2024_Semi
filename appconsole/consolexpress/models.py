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

class Tarjeta(models.Model):
    numero_tarjeta = models.CharField(max_length=16)  # Número único para evitar duplicados
    titular = models.CharField(max_length=100)  # Nombre del titular
    fecha_vencimiento = models.DateField()  # Fecha en formato AAAA-MM-DD
    tipo_tarjeta = models.CharField(max_length=50, choices=[('credito', 'Crédito'), ('debito', 'Débito')])  # Tipo de tarjeta
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Saldo disponible
    cvv = models.CharField(max_length=3)  # Código de seguridad (3 dígitos)

    def save(self, *args, **kwargs):
    # Eliminar espacios y asegurarse de que el número de tarjeta tenga exactamente 16 dígitos
        self.numero_tarjeta = self.numero_tarjeta.replace(' ', '')  # Eliminar espacios
        self.numero_tarjeta = self.numero_tarjeta[:16]  # Limitar a 16 caracteres
        super().save(*args, **kwargs)

    def __str__(self):
        return f"**** **** **** {self.numero_tarjeta[-4:]}"  # Mostrar solo los últimos 4 dígitos de la tarjeta




    
    
    
    