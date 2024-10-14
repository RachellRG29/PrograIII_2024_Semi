from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def peliculas(request):
    return render(request, 'pelicula/index.html')