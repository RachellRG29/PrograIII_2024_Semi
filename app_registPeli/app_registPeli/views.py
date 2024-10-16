from django.shortcuts import render, redirect, get_object_or_404
from peliculas.models import Peliculas
from peliculas.forms import PeliculaForm

def login(request):
    return render(request, 'pelicula/index_login.html')
# Vista para la página principal de las películas
def peliculas(request):
    # Si el método es POST, entonces estamos agregando una película
    if request.method == 'POST':
        form = PeliculaForm(request.POST, request.FILES)  # Manejo de archivos con request.FILES
        if form.is_valid():
            form.save()  # Guarda la película en la base de datos
            return redirect('peliculas')  # Redirige a la misma página después de guardar
    else:
        form = PeliculaForm()  # Si no es POST, se muestra el formulario vacío

    # Obtiene todas las películas de la base de datos
    peliculas = Peliculas.objects.all()

    # Renderiza la plantilla con el formulario y las películas
    return render(request, 'pelicula/index.html', {
        'form': form,
        'peliculas': peliculas  
    })

# Vista para ver una película en detalle
def ver_pelicula(request, id):
    pelicula = get_object_or_404(Peliculas, id=id) 
    return render(request, 'pelicula/ver.html', {'pelicula': pelicula})

# Vista para editar una película
def editar_pelicula(request, id):
    pelicula = get_object_or_404(Peliculas, id=id)  
    if request.method == 'POST':
        form = PeliculaForm(request.POST, request.FILES, instance=pelicula)
        if form.is_valid():
            form.save()
            return redirect('peliculas')
    else:
        form = PeliculaForm(instance=pelicula)
    return render(request, 'pelicula/editar.html', {'form': form, 'pelicula': pelicula})

# Vista para eliminar una película
def eliminar_pelicula(request, id):
    pelicula = get_object_or_404(Peliculas, id=id) 
    if request.method == 'POST':
        pelicula.delete()
        return redirect('peliculas')
    return render(request, 'pelicula/eliminar.html', {'pelicula': pelicula})
