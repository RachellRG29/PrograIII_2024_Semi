from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.shortcuts import render
from .models import consola  #MODELO
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib.auth.decorators import login_required #para registrar y no permitir q cualquiera ingrese
from django.contrib.auth.models import User #Para conectar con la base de datos y mandar los usuarios
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages #mandar mensajes con sweetalert2
from nltk.chat.util import Chat, reflections
from fuzzywuzzy import fuzz
from .chatbot_logic import pairs
from .models import consola
import json
import time
from .models import Tarjeta
from datetime import datetime
from decimal import Decimal, InvalidOperation
from django.urls import reverse


# Create your views here.
def index_inicio(request):
    return render(request, 'index_inicio.html')

#DEF PARA LOGEARSE EN LA PAGINA CONSOLEXPRESS
def index_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:  # Verifica si el usuario es superusuario
                return redirect('crud_admi')  # Redirige a la vista de administración
            else:
                return redirect('index_pant_prin')  # Redirige a la página principal si no es superusuario
        else:
            messages.error(request, "Credenciales incorrectas.")
            return redirect('index_login')  # Redirige al login si falla

    return render(request, 'index_login.html')

#DEF PARA REGISTRAR USUARIOS
def index_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "El nombre de usuario ya está en uso.")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "El correo electrónico ya está en uso.")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "Usuario registrado correctamente.")
                return redirect('index_login')  # Redirigir a la página de inicio de sesión después del registro
        else:
            messages.error(request, "Las contraseñas no coinciden.")

    return render(request, 'index_register.html')

#Para logout o salir de sesion
def user_logout(request):
    logout(request)
    return redirect('index_inicio')

# Pantalla principal
#@login_required
def index_pant_prin(request):
    consolas = consola.objects.all()  # Recupera todos los objetos de la tabla consola
    return render(request, 'index_pant_prin.html', {'consolas': consolas})
   
    
# Verificación de permisos para superusuario
def superuser_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, "Acceso denegado: no tienes permisos de administrador.")
            return redirect('index_pant_prin')  # Redirige a la pantalla principal
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func

#validar crud admin solo para administradores
@login_required
@superuser_required
def crud_admi(request):
    return render(request, 'crud_admi.html')

# Función para consultar todas las consolas
@login_required
@superuser_required
def consultar_consolas(request):
    datos = consola.objects.all()  # Obtener todas las consolas
    data = [
        {
            'id': c.id,
            'imagen': f"{settings.MEDIA_URL}{c.imagen}" if c.imagen else None,  # URL completa de la imagen
            'codigo': c.codigo,
            'nombre': c.nombre,
            'descripcion': c.descripcion,
            'presentacion': c.presentacion,
            'categoria': c.categoria,
            'marca': c.marca,
            'precio': c.precio,
            'stock': c.stock,
        }
        for c in datos
    ]
    return JsonResponse(data, safe=False)

#Consultar todas las consolas unicamente para ver en pantalla principal
#@login_required
def consultar_consolas_pant_prin(request):
    datos = consola.objects.all()  
    data = [
        {
            'id': c.id,
            'imagen': f"{settings.MEDIA_URL}{c.imagen}" if c.imagen else None,  # URL completa de la imagen
            'codigo': c.codigo,
            'nombre': c.nombre,
            'descripcion': c.descripcion,
            'presentacion': c.presentacion,
            'categoria': c.categoria,
            'marca': c.marca,
            'precio': c.precio,
            'stock': c.stock,
        }
        for c in datos
    ]
    return JsonResponse(data, safe=False)

# Función para guardar consola
@login_required
@superuser_required
def guardar_consola(request):
    if request.method == 'POST':
        consola_id = request.POST.get('id')  # Obtener el id de consola si existe

        required_fields = ['codigo', 'nombre', 'descripcion', 'presentacion', 'categoria', 'marca', 'precio', 'stock']
        for field in required_fields:
            if field not in request.POST:
                return JsonResponse({'msg': 'error', 'error': f'El campo {field} es requerido'}, status=400)

        # Si consola_id existe, estamos en modo edición; de lo contrario, creamos una nueva instancia
        if consola_id:
            consola_instance = get_object_or_404(consola, id=consola_id)
            action = 'updated'
        else:
            consola_instance = consola()  # Nueva instancia
            action = 'created'

        # Asignación de valores
        consola_instance.codigo = request.POST['codigo']
        consola_instance.nombre = request.POST['nombre']
        consola_instance.descripcion = request.POST['descripcion']
        consola_instance.presentacion = request.POST['presentacion']
        consola_instance.categoria = request.POST['categoria']
        consola_instance.marca = request.POST['marca']
        consola_instance.precio = request.POST['precio']
        consola_instance.stock = request.POST['stock']
        
        # Actualización de imagen solo si es necesario
        if 'imagen' in request.FILES:
            consola_instance.imagen = request.FILES['imagen']
        
        consola_instance.save()

        return JsonResponse({
            'msg': 'success',
            'action': action,
            'consola': {
                'id': consola_instance.id,
                'codigo': consola_instance.codigo,
                'imagen': f"{settings.MEDIA_URL}{consola_instance.imagen}" if consola_instance.imagen else None,
                'nombre': consola_instance.nombre,
                'descripcion': consola_instance.descripcion,
                'presentacion': consola_instance.presentacion,
                'categoria': consola_instance.categoria,
                'marca': consola_instance.marca,
                'precio': consola_instance.precio,
                'stock': consola_instance.stock,
            }
        })

    return JsonResponse({'msg': 'error', 'error': 'Método no permitido'}, status=405)

# Función para consultar 1 consola y editarla
@login_required
@superuser_required
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
                    'presentacion': consola_obj.presentacion,
                    'categoria': consola_obj.categoria,
                    'marca': consola_obj.marca,
                    'precio': consola_obj.precio,
                    'stock': consola_obj.stock,
                }
                return JsonResponse(data)
            except consola.DoesNotExist:
                return JsonResponse({'msg': 'error', 'error': 'Consola no encontrada'}, status=404)

    return JsonResponse({'msg': 'error', 'error': 'Método no permitido'}, status=405)

# Función para editar consola
@login_required
@superuser_required
def editar_consola(request):
    if request.method == 'POST':
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
            required_fields = ['codigo', 'nombre', 'descripcion', 'presentacion','categoria', 'marca', 'precio', 'stock','imagen']
            for field in required_fields:
                if field not in data:
                    return JsonResponse({'error': f'Falta el campo: {field}'}, status=400)

            try:
                consola_obj = consola.objects.get(id=id_consola)
                consola_obj.codigo = data['codigo']
                consola_obj.nombre = data['nombre']
                consola_obj.descripcion = data['descripcion']
                consola_obj.presentacion = data['presentacion']
                consola_obj.categoria = data['categoria']
                consola_obj.marca = data['marca']
                consola_obj.precio = data['precio']
                consola_obj.stock = data['stock']

                # Actualizar la imagen si se proporciona
                if 'imagen' in request.FILES:
                    consola_obj.imagen = request.FILES['imagen']

                consola_obj.save()

                return JsonResponse({
                    'msg': 'success',
                    'consola': {
                        'id': consola_obj.id,
                        'codigo': consola_obj.codigo,
                        'nombre': consola_obj.nombre,
                        'descripcion': consola_obj.descripcion,
                        'presentacion': consola_obj.presentacion,
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
@login_required
@superuser_required
def eliminar_consola(request):
    if request.method == 'DELETE':
        data = json.loads(request.body)
        consola_id = data.get('id')
        consola_obj = get_object_or_404(consola, id=consola_id)
        consola_obj.delete()  # Eliminar el objeto
        return JsonResponse({'msg': 'success'})
    return JsonResponse({'msg': 'error'}, status=400)

@login_required
@superuser_required
def verificar_codigo_existente(request):
    if request.method == 'GET':
        codigo = request.GET.get('codigo')
        if codigo:
            existe = consola.objects.filter(codigo=codigo).exists()  # Verificar si el código ya existe
            return JsonResponse({'existe': existe})
        return JsonResponse({'existe': False})  # Si no hay código, devuelve false
    return JsonResponse({'msg': 'error', 'error': 'Método no permitido'}, status=405) 

#CHATBOT IA IMPLEMENTOS
# Inicializando el chatbot
chatbot = Chat(pairs, reflections)

# Función para encontrar la pregunta más cercana usando fuzzywuzzy
def get_closest_match(user_input):
    closest_match = None
    highest_score = 0
    for pattern, responses in pairs:
        score = fuzz.ratio(user_input, pattern)
        if score > highest_score:
            highest_score = score
            closest_match = responses[0]
    return closest_match if highest_score >= 60 else "Lo siento, no entiendo lo que quieres consultar."

#Chatbot ia
def chatbotIA(request):
    return render(request, 'chatbotIA.html')

@csrf_exempt
def chat(request):
    if request.method == "POST":
        user_input = request.POST.get("message", "")
        response = chatbot.respond(user_input)
        if response is None:
            response = get_closest_match(user_input)
        time.sleep(0.3)  # Esperar 0.3 segundos antes de enviar la respuesta
        return JsonResponse({"response": response})
    return JsonResponse({"error": "Invalid request"}, status=400)

def vistaprincipal_producto(request):
    return render(request, 'vistaprincipal_producto.html') 

def detalle_producto(request, codigo):
    try:
        producto = consola.objects.get(codigo=codigo)  # Recupera el producto usando el código
        return render(request, 'detalle_producto.html', {'producto': producto})  # Pasa el producto a la plantilla
    except consola.DoesNotExist:
        return render(request, '404.html')
    
def crear_y_listar_tarjetas(request):
    if request.method == "POST":
        numero_tarjeta = request.POST['numero_tarjeta']
        titular = request.POST['titular']
        fecha_vencimiento = request.POST['fecha_vencimiento']
        tipo_tarjeta = request.POST['tipo_tarjeta']
        saldo = request.POST['saldo']

        # Crear una nueva tarjeta
        Tarjeta.objects.create(
            numero_tarjeta=numero_tarjeta,
            titular=titular,
            fecha_vencimiento=fecha_vencimiento,
            tipo_tarjeta=tipo_tarjeta,
            saldo=saldo
        )

        # Mensaje de éxito
        messages.success(request, '¡Tarjeta creada con éxito!')

    # Obtener todas las tarjetas
    tarjetas = Tarjeta.objects.all()

    return render(request, 'vistaprincipal_producto.html', {'tarjetas': tarjetas})

@login_required
def procesar_pago(request):
    if request.method == "POST":
        # Obtener y limpiar el número de tarjeta (eliminar espacios)
        numero_tarjeta = request.POST.get('numero_tarjeta').replace(' ', '')  # Eliminar espacios
        cvv = request.POST.get('cvv')
        fecha_vencimiento = request.POST.get('fecha_vencimiento')
        total = request.POST.get('total')

        # Imprimir el número de tarjeta recibido para verificar
        print(f"Numero de tarjeta recibido: '{numero_tarjeta}'")

        # Validar entrada de datos
        try:
            total = Decimal(total)
        except (InvalidOperation, ValueError):
            messages.error(request, "El valor total es inválido.")
            return redirect('pago')

        try:
            # Buscar la tarjeta en la base de datos sin espacios
            tarjeta = Tarjeta.objects.get(numero_tarjeta=numero_tarjeta)
            print(f"Numero de tarjeta encontrado en base de datos: '{tarjeta.numero_tarjeta}'")
        except Tarjeta.DoesNotExist:
            print("No se encontró la tarjeta.")
            messages.error(request, "El número de tarjeta no es válido.")
            return redirect('pago')

        # Verificar fecha de vencimiento
        if tarjeta.fecha_vencimiento < datetime.now().date():
            messages.error(request, "La tarjeta ha expirado.")
            return redirect('pago')

        # Verificar el CVV
        if tarjeta.cvv != cvv:
            messages.error(request, "El CVV es incorrecto.")
            return redirect('pago')

        # Verificar saldo suficiente
        if tarjeta.saldo < total:
            messages.error(request, "No tienes saldo suficiente en la tarjeta.")
            return redirect('pago')

        # Procesar el pago (restar saldo)
        tarjeta.saldo -= total
        tarjeta.save()

        # Mensaje de éxito
        messages.success(request, '¡Pago realizado con éxito!')

        # Redirigir al usuario a la pantalla principal
        return redirect('index_pant_prin')

    # Si no es un POST, renderizar la página de pago
    return render(request, 'pago.html')