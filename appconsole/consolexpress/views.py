from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import consola
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index_inicio(request):
    return render(request, 'index_inicio.html')

def index_login(request):
    return render(request, 'index_login.html')

def index_register(request):
    return render(request, 'index_register.html')

def index_pant_prin(request):
    return render(request, 'index_pant_prin.html')

def crud_admi(request):
    return render(request, 'crud_admi.html')

def consultar_consolas(request):
    datos = consola.objects.values('id', 'codigo', 'nombre', 'descripcion', 'categoria', 'marca', 'precio', 'stock')
    return JsonResponse(list(datos), safe=False)

def vistaprincipal_producto(request):
    return render(request, 'vistaprincipal_producto.html')