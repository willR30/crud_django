from django import urls
from django.contrib import admin
from django.urls import path, include

#aqui debo de gestionar las rutas de las paguinas web que quiero mostrar
urlpatterns = [
    path('admin/', admin.site.urls),
    #incluimos las ruta de Autenticacion
    path('', include('crud_django.urls')),
]