from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
import json
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
        # Validación básica de campos requeridos
        required_fields = ['codigo', 'nombre', 'descripcion', 'categoria', 'marca', 'precio', 'stock']
        for field in required_fields:
            if field not in request.POST:
                return JsonResponse({'msg': 'error', 'error': f'El campo {field} es requerido'}, status=400)
        
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

def editar_consola(request):
    if request.method == 'POST':
        consola = consultar_consolas.objects.get(id=request.POST['id'])
        consola.codigo = request.POST['codigo']
        consola.nombre = request.POST['nombre']
        consola.descripcion = request.POST['descripcion']
        consola.categoria = request.POST['categoria']
        consola.marca = request.POST['marca']
        consola.precio = request.POST['precio']
        consola.stock = request.POST['stock']
        consola.save()
        return JsonResponse({'msg': 'success'})


# Función para eliminar consola
@csrf_exempt
def eliminar_consola(request):
    if request.method == 'DELETE':
        data = json.loads(request.body)
        consola_id = data.get('id')
        consola_obj = get_object_or_404(consola, id=consola_id)
        consola_obj.delete()  # Eliminar el objeto
        return JsonResponse({'msg': 'success'})
    return JsonResponse({'msg': 'error'}, status=400)


def vistaprincipal_producto(request):
    return render(request, 'vista_principal_producto.html')  