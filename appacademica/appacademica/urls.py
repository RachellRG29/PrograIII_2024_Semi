from django.contrib import admin
from django.urls import path
from academica.views import index, vista, consultar_alumnos, guardar_alumno, consultar_docentes, guardar_docente, consultar_materias, guardar_materia

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('vista/<str:form>/', vista),
    path('consultar_alumnos/', consultar_alumnos),
    path('guardar_alumno/', guardar_alumno),
    path('consultar_docentes/', consultar_docentes),
    path('guardar_docente/', guardar_docente),
    path('consultar_materias/', consultar_materias),
    path('guardar_materia/', guardar_materia),
]
