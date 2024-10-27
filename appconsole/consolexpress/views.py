from django.shortcuts import render
from django.http import JsonResponse
from .models import consola  # Asegúrate de que el modelo se llame correctamente
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
    datos = consola.objects.values('id', 'imagen', 'codigo', 'nombre', 'descripcion', 'categoria', 'marca', 'precio', 'stock')
    return JsonResponse(list(datos), safe=False)

@csrf_exempt  # Asegúrate de entender las implicaciones de deshabilitar CSRF
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
                'imagen': nueva_consola.imagen.url,  # URL de la imagen
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

@csrf_exempt  
def eliminar_consola(request, id):
    if request.method == 'DELETE':  
        try:
            consola_obj = consola.objects.get(id=id)
            consola_obj.delete()
            return JsonResponse({'msg': 'success'})
        except consola.DoesNotExist:
            return JsonResponse({'msg': 'error', 'error': 'Consola no encontrada'}, status=404)
    return JsonResponse({'msg': 'error', 'error': 'Método no permitido'}, status=405)

@csrf_exempt  
def editar_consola(request, id):
    if request.method == 'PUT':
        try:
            consola_obj = consola.objects.get(id=id)
            consola_obj.codigo = request.POST.get('codigo', consola_obj.codigo)
            consola_obj.nombre = request.POST.get('nombre', consola_obj.nombre)
            consola_obj.descripcion = request.POST.get('descripcion', consola_obj.descripcion)
            consola_obj.categoria = request.POST.get('categoria', consola_obj.categoria)
            consola_obj.marca = request.POST.get('marca', consola_obj.marca)
            consola_obj.precio = request.POST.get('precio', consola_obj.precio)
            consola_obj.stock = request.POST.get('stock', consola_obj.stock)

            if 'imagen' in request.FILES:
                consola_obj.imagen = request.FILES['imagen']

            consola_obj.save()
            return JsonResponse({'msg': 'success'})
        except consola.DoesNotExist:
            return JsonResponse({'msg': 'error', 'error': 'Consola no encontrada'}, status=404)
    return JsonResponse({'msg': 'error', 'error': 'Método no permitido'}, status=405)

def vistaprincipal_producto(request):
    return render(request, 'vista_principal_producto.html')  