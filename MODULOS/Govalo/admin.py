from django.contrib import admin

from MODULOS.Govalo.models import Cliente
from MODULOS.Govalo.models import *

# Register your models here.

admin.site.register (Cliente)
admin.site.register (GYO)
admin.site.register (Pedidos)
admin.site.register (Morosidad)