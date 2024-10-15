from django import forms
from .models import Peliculas

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Peliculas
        fields = ['imagen', 'titulo', 'descripcion', 'categoria', 'clasificacion', 'fecha_estreno', 'director', 'duracion', 'idioma']
