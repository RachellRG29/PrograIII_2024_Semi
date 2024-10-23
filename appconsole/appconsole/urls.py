from django.contrib import admin
from django.urls import path
from consolexpress.views import index_inicio, index_login, index_register, index_pant_prin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_inicio, name='index_inicio'),
    path('login/', index_login, name='index_login'), 
    path('register/', index_register, name='index_register'),  
    path('pantalla_prin/', index_pant_prin, name='index_pant_prin'),  
]
