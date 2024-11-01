from django.shortcuts import render,get_object_or_404
from django.views.decorators.http import require_http_methods
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
        consola_id = request.POST.get('id')  # Obtener el id de consola si existe

        # Validación básica de campos requeridos
        required_fields = ['codigo', 'nombre', 'descripcion', 'categoria', 'marca', 'precio', 'stock']
        for field in required_fields:
            if field not in request.POST:
                return JsonResponse({'msg': 'error', 'error': f'El campo {field} es requerido'}, status=400)

        # Verificar si consola_id existe; si sí, se trata de una edición
        if consola_id:
            consola_instance = get_object_or_404(consola, id=consola_id)
            consola_instance.codigo = request.POST['codigo']
            consola_instance.nombre = request.POST['nombre']
            consola_instance.descripcion = request.POST['descripcion']
            #consola_instance.categoria = request.POST['categoria']
            consola_instance= consola.CATEGORIA_CHOICES
            return render(request, 'consolas.html',{'consola_instance':'categoria'})
            consola_instance.marca = request.POST['marca']
            consola_instance.precio = request.POST['precio']
            consola_instance.stock = request.POST['stock']
            if 'imagen' in request.FILES:
                consola_instance.imagen = request.FILES['imagen']
            consola_instance.save()
            action = 'updated'
        else:
            # Si no hay id, entonces es una nueva consola
            consola_instance = consola(
                codigo=request.POST['codigo'],
                nombre=request.POST['nombre'],
                descripcion=request.POST['descripcion'],
                categoria=request.POST['categoria'],
                marca=request.POST['marca'],
                precio=request.POST['precio'],
                stock=request.POST['stock'],
            )
            if 'imagen' in request.FILES:
                consola_instance.imagen = request.FILES['imagen']
            consola_instance.save()
            action = 'created'

        return JsonResponse({
            'msg': 'success',
            'action': action,
            'consola': {
                'codigo': consola_instance.codigo,
                'imagen': f"{settings.MEDIA_URL}{consola_instance.imagen}" if consola_instance.imagen else None,
                'nombre': consola_instance.nombre,
                'descripcion': consola_instance.descripcion,
                'categoria': consola_instance.categoria,
                'marca': consola_instance.marca,
                'precio': consola_instance.precio,
                'stock': consola_instance.stock,
                'id': consola_instance.id,
            }
        })
    return JsonResponse({'msg': 'error', 'error': 'Método no permitido'}, status=405)



@csrf_exempt
@require_http_methods(["POST"])
def editar_consola(request, id):
    if request.method == 'POST':
        # Cargar el cuerpo de la solicitud
        data = json.loads(request.body)

        # Obtener la consola a editar
        consola_instance = get_object_or_404(consola, id=id)

        # Actualizar los campos
        consola_instance.codigo = data.get('codigo', consola_instance.codigo)
        consola_instance.nombre = data.get('nombre', consola_instance.nombre)
        consola_instance.descripcion = data.get('descripcion', consola_instance.descripcion)
        consola_instance.categoria = data.get('categoria', consola_instance.categoria)
        consola_instance.marca = data.get('marca', consola_instance.marca)
        consola_instance.precio = data.get('precio', consola_instance.precio)
        consola_instance.stock = data.get('stock', consola_instance.stock)

        # Guardar los cambios
        consola_instance.save()

        # Enviar la respuesta de éxito
        return JsonResponse({
            'msg': 'success',
            'consola': {
                'id': consola_instance.id,
                'codigo': consola_instance.codigo,
                'nombre': consola_instance.nombre,
                'descripcion': consola_instance.descripcion,
                'categoria': consola_instance.categoria,
                'marca': consola_instance.marca,
                'precio': consola_instance.precio,
                'stock': consola_instance.stock,
            }
        })
    return JsonResponse({'msg': 'error', 'error': 'Método no permitido'}, status=405)



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