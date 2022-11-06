from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from.forms import *
from .forms import ClienteForms
from.models import*
# Create your views here.
def inicio(request):
    return render(request,'C:/MOVALO/MODULOS/Govalo/templates/index.html')

def prueba(request):
    return render(request,'C:/MOVALO/MODULOS/Govalo/templates/prueba.html')

def clienteForms(request, nombre, apellido ):
    cliente = ClienteForms(nombre=nombre, apellido=apellido)
    clienteForms.save()

