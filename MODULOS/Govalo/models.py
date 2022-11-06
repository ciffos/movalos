from django.db import models
from unittest.util import _MAX_LENGTH
from django.db import models
from typing_extensions import Self

# Create your models here.
class Cliente(models.Model):
    nombre =      models.CharField(max_length=50)
    apellido =    models.CharField(max_length=50)
    direccion =   models.CharField(max_length=50)
    email =       models.CharField(max_length=50)
    dni =         models.CharField(max_length=8,primary_key= True)
    telefono =    models.IntegerField(max_length=10) 
    sexos=[
        ("f","Femenino"),
        ("m", "Masculino"),
    ]
    sexo = models.CharField(max_length=1, choices=sexos,default="m") 
    def __str__(self):
        txt = "{0}"
        return txt.format(self.nombre , self.apellido)

def nombreCompleto (self):
    txt ="{0},{1},{2}"
    return txt.format(Self.apellido, Self.nombre, Self.email)

class GYO (models.Model):

    grupo_y_orden=models.CharField(max_length=8,primary_key=True)
    modelo_unidad =models.CharField(max_length=15)
    Estado_del_Suscriptor= models.CharField(max_length=40)
    inicio_de_Suscripcion = models.DateField()
    Cliente = models.ForeignKey(Cliente,null=False, blank=False, on_delete=models.CASCADE),
    estatusP=[
        ("P","Pendiente"),
        ("A", "Aprobado"),
    ]
    Estado_de_Pedido = models.CharField(max_length=1, choices=estatusP,default="P")
    def __str__(self):
        txt = "{0}"
        return txt.format(self.grupo_y_orden)
    
    

class Pedidos(models.Model):
    suscripcion = models.IntegerField(max_length=13,primary_key=True)
    unidad_Suscripta = models.CharField(max_length=30)
    unidad_Solicitada = models.CharField(max_length=30)
    Fecha_ingreso_Pedido = models.DateField()

class Morosidad(models.Model):
    status_cartera = models.CharField(max_length=30,primary_key=True)
    cantidad_de_cuotas_impagas = models.IntegerField(max_length=3)
    cantidad_de_cuotas_pagas = models.IntegerField(max_length=3)
    Cliente = models.ForeignKey(Cliente, null= False, blank= False, on_delete=models.CASCADE)
    GYO = models.ForeignKey(GYO, null= False, blank= False, on_delete=models.CASCADE)
