from django.shortcuts import render
from django.http import JsonResponse
from .models import consola  # Asegúrate de que el modelo se llame correctamente
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

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
    datos = consola.objects.all()  # Obtener todas las consolas
    data = [
        {
            'id': c.id,
            'imagen': f"{settings.MEDIA_URL}{c.imagen}" if c.imagen else None,  # URL completa de la imagen
            'codigo': c.codigo,
            'nombre': c.nombre,
            'descripcion': c.descripcion,
            'categoria': c.categoria,
            'marca': c.marca,
            'precio': c.precio,
            'stock': c.stock,
        }
        for c in datos
    ]
    return JsonResponse(data, safe=False)

@csrf_exempt  
def guardar_consola(request):
    if request.method == 'POST':
        nueva_consola = consola(
            codigo=request.POST['codigo'],
            nombre=request.POST['nombre'],
            descripcion=request.POST['descripcion'],
            categoria=request.POST['categoria'],
            marca=request.POST['marca'],
            precio=request.POST['precio'],
            stock=request.POST['stock'],
        )
        if 'imagen' in request.FILES:
            nueva_consola.imagen = request.FILES['imagen']
        nueva_consola.save()

        return JsonResponse({
            'msg': 'success',
            'consola': {
                'codigo': nueva_consola.codigo,
                'imagen': f"{settings.MEDIA_URL}{nueva_consola.imagen}" if nueva_consola.imagen else None,  # URL de la imagen
                'nombre': nueva_consola.nombre,
                'descripcion': nueva_consola.descripcion,
                'categoria': nueva_consola.categoria,
                'marca': nueva_consola.marca,
                'precio': nueva_consola.precio,
                'stock': nueva_consola.stock,
                'id': nueva_consola.id,  # ID para eliminar más tarde
            }
        })
    return JsonResponse({'msg': 'error', 'error': 'Método no permitido'}, status=405)

def vistaprincipal_producto(request):
    return render(request, 'vista_principal_producto.html')  