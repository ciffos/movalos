from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .forms import *
from .models import*
from django.db.models import Q
# Create your views here.
def inicio(request):
    return render(request,'index.html')

def buscar_cliente(request):
    
    return render(request, 'buscar_cliente.html')

class Buscar(ListView):
    model = Cliente
    template_name = "buscar_cliente.html"
    def get_queryset(self):  # new
        query = self.request.GET.get("dni")
        if query=="":
            response = 'cliente no encontrado'
            HttpResponseRedirect('/Govalo/', {'response':response})
        else:    
            object_list = Cliente.objects.filter(Q(dni__icontains=query))       
            return (object_list)
        
