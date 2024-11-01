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
    if request.method in ['POST', 'PUT']:
        consola_id = request.POST.get('id')  # Obtener el id de consola si existe

        required_fields = ['codigo', 'nombre', 'descripcion', 'categoria', 'marca', 'precio', 'stock']
        for field in required_fields:
            if field not in request.POST:
                return JsonResponse({'msg': 'error', 'error': f'El campo {field} es requerido'}, status=400)

        if consola_id:  # Si estamos editando
            consola_instance = get_object_or_404(consola, id=consola_id)
            consola_instance.codigo = request.POST['codigo']
            consola_instance.nombre = request.POST['nombre']
            consola_instance.descripcion = request.POST['descripcion']
            consola_instance.categoria = request.POST['categoria']
            consola_instance.marca = request.POST['marca']
            consola_instance.precio = request.POST['precio']
            consola_instance.stock = request.POST['stock']
            if 'imagen' in request.FILES:
                consola_instance.imagen = request.FILES['imagen']
            consola_instance.save()
            action = 'updated'
        else:  # Si estamos agregando
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
def consultar_consola_edit(request):
    if request.method == 'GET':
        consola_id = request.GET.get('id')
        if consola_id:
            try:
                consola_obj = consola.objects.get(id=consola_id)
                data = {
                    'id': consola_obj.id,
                    'imagen': f"{settings.MEDIA_URL}{consola_obj.imagen}" if consola_obj.imagen else None,
                    'codigo': consola_obj.codigo,
                    'nombre': consola_obj.nombre,
                    'descripcion': consola_obj.descripcion,
                    'categoria': consola_obj.categoria,
                    'marca': consola_obj.marca,
                    'precio': consola_obj.precio,
                    'stock': consola_obj.stock,
                }
                return JsonResponse(data)
            except consola.DoesNotExist:
                return JsonResponse({'msg': 'error', 'error': 'Consola no encontrada'}, status=404)

    return JsonResponse({'msg': 'error', 'error': 'Método no permitido'}, status=405)

@csrf_exempt
def editar_consola(request):
    if request.method == 'PUT':
        import json
        try:
            if not request.body:
                return JsonResponse({'error': 'Cuerpo de la solicitud vacío'}, status=400)

            data = json.loads(request.body)

            # Comprobar que el ID de la consola está presente
            id_consola = data.get('id')
            if id_consola is None:
                return JsonResponse({'error': 'ID de consola no proporcionado'}, status=400)

            # Verificar que todos los campos necesarios están presentes
            required_fields = ['codigo', 'nombre', 'descripcion', 'categoria', 'marca', 'precio', 'stock']
            for field in required_fields:
                if field not in data:
                    return JsonResponse({'error': f'Falta el campo: {field}'}, status=400)

            try:
                consola_obj = consola.objects.get(id=id_consola)
                consola_obj.codigo = data['codigo']
                consola_obj.nombre = data['nombre']
                consola_obj.descripcion = data['descripcion']
                consola_obj.categoria = data['categoria']
                consola_obj.marca = data['marca']
                consola_obj.precio = data['precio']
                consola_obj.stock = data['stock']

                # Actualizar la imagen si se proporciona
                if 'imagen' in data:
                    consola_obj.imagen = data['imagen']

                consola_obj.save()

                return JsonResponse({
                    'msg': 'success',
                    'consola': {
                        'id': consola_obj.id,
                        'codigo': consola_obj.codigo,
                        'nombre': consola_obj.nombre,
                        'descripcion': consola_obj.descripcion,
                        'categoria': consola_obj.categoria,
                        'marca': consola_obj.marca,
                        'precio': str(consola_obj.precio),
                        'stock': consola_obj.stock,
                        'imagen': consola_obj.imagen.url if consola_obj.imagen else ''
                    }
                })
            except consola.DoesNotExist:
                return JsonResponse({'error': 'Consola no encontrada'}, status=404)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)




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