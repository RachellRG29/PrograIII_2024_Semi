from django.urls import path
from ..app_registPeli import views

urlpatterns = [
    path('peliculas', views.peliculas, name='peliculas'),
]