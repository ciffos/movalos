from socket import fromshare
from django import forms
from .models import sexos
from .models import estatusP


class ClienteForms(forms.Form):
    nombre =      forms.CharField(max_length=50)
    apellido =    forms.CharField(max_length=50)
    direccion =   forms.CharField(max_length=50)
    email =       forms.CharField()
    dni =         forms.CharField(max_length=50)
    telefono =    forms.IntegerField() 
    sexo = forms.CharField(widget=forms.Select(choices=sexos))
    def __str__(self):
        txt = "{0}"
        return txt.format(self.nombre , self.apellido)

class GYOForms(forms.Form):
    grupo_y_orden=     forms.CharField(max_length=8)
    modelo_unidad =    forms.CharField(max_length=15)
    Estado_del_Suscriptor=    forms.CharField(max_length=40)
    inicio_de_Suscripcion =   forms.DateField()
    Estado_de_Pedido = forms.CharField(widget=forms.Select(choices=estatusP))

