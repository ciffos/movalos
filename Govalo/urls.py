from django.contrib import admin
from django.urls import path
from .views import * 

urlpatterns = [
    
    path('index/', inicio),
    path('buscar_cliente/',buscar_cliente, name='buscar_cliente'),
    path('buscar/',Buscar.as_view(), name='buscar'),
    
]
