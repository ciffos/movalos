from socket import fromshare
from django import forms

from .views import *
from .views import clienteForms

class ClienteForms(forms.Form):
    nombre =      forms.CharField(max_length=50)
    apellido =    forms.CharField(max_length=50)
    direccion =   forms.CharField(max_length=50)
    email =       forms.CharField()
    dni =         forms.CharField(max_length=50)
    telefono =    forms.IntegerField(max_length=10) 
    sexos=[
        ("f","Femenino"),
        ("m", "Masculino"),
    ]
    sexo = forms.CharField(max_length=1, choices=sexos,default="m") 
    def __str__(self):
        txt = "{0}"
        return txt.format(self.nombre , self.apellido)

class GYOForms(forms.Form):
    grupo_y_orden=     forms.CharField(max_length=8,primary_key=True)
    modelo_unidad =    forms.CharField(max_length=15)
    Estado_del_Suscriptor=    forms.CharField(max_length=40)
    inicio_de_Suscripcion =   forms.DateField()
    Cliente =forms.ForeignKey(clienteForms,null=False, blank=False, on_delete=forms.CASCADE),
    estatusP=[
        ("P","Pendiente"),
        ("A", "Aprobado"),
    ]
    Estado_de_Pedido = forms.CharField(max_length=1, choices=estatusP,default="P")

