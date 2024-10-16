from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import peliculas, ver_pelicula, editar_pelicula, eliminar_pelicula

urlpatterns = [
    path('peliculas/', peliculas, name='peliculas'),  
    path('editar/<int:id>/', editar_pelicula, name='editar_pelicula'),
    path('eliminar/<int:id>/', eliminar_pelicula, name='eliminar_pelicula'),
    path('ver/<int:id>/', ver_pelicula, name='ver_pelicula'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
