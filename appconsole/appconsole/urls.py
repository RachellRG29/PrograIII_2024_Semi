from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from consolexpress.views import (index_inicio, index_login, user_logout, index_register, index_pant_prin, 
                                 crud_admi, guardar_consola, consultar_consolas, editar_consola, consultar_consola_edit, eliminar_consola, verificar_codigo_existente,
                                 consultar_consolas_pant_prin,vistaprincipal_producto,chatbotIA,chat)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_inicio, name='index_inicio'),
    path('login/', index_login, name='index_login'), 
    path('logout/', user_logout, name='user_logout'), 
    path('register/', index_register, name='index_register'),  
    path('pantalla_prin/', index_pant_prin, name='index_pant_prin'),
    path('crud_admi/', crud_admi, name='crud_admi'), 
    path('guardar_consola/', guardar_consola, name='guardar_consola'), 
    path('consultar_consolas/', consultar_consolas, name='consultar_consolas'),
    path('editar_consola/', editar_consola, name='editar_consola'), 
    path('consultar_consola_edit/', consultar_consola_edit, name='consultar_consola_edit'),
    path('consultar_consolas_pant_prin/', consultar_consolas_pant_prin, name='consultar_consolas_pant_prin'),
    path('eliminar_consola/', eliminar_consola, name='eliminar_consola'),
    path('verificar_codigo_existente/', verificar_codigo_existente, name='verificar_codigo_existente'),
    path('vistaprincipal_producto/', vistaprincipal_producto, name='vistaprincipal_producto'),   
    path('chatbotIA/', chatbotIA, name='chatbotIA'), 
    path('chat/', chat, name='chat'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    