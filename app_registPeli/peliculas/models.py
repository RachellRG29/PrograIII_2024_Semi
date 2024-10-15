import random
from django.db import models

# Modelo para Categorías
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

# Modelo para Películas
class Peliculas(models.Model):
    N_id = models.CharField(max_length=6, unique=True, editable=False, default=lambda: str(random.randint(100000, 999999)))
    imagen = models.ImageField(upload_to='peliculas/')
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=100)
    clasificacion = models.CharField(max_length=10)
    fecha_estreno = models.DateField()
    director = models.CharField(max_length=100)
    duracion = models.IntegerField()  
    idioma = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo

    def get_acciones(self):
        return f'<a href="/pelicula/{self.N_id}/ver">Ver</a> | <a href="/pelicula/{self.N_id}/editar">Editar</a> | <a href="/pelicula/{self.N_id}/eliminar">Eliminar</a>'

    def save(self, *args, **kwargs):
        # Verificación de unicidad del N_id
        if not self.N_id:
            self.N_id = str(random.randint(100000, 999999))
            while Peliculas.objects.filter(N_id=self.N_id).exists():
                self.N_id = str(random.randint(100000, 999999))
        super().save(*args, **kwargs)
