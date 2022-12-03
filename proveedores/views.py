from django.shortcuts import render
from django.http import HttpResponse
from proveedores.models import Proveedor
# Create your views here.

def proveedores (request):
    #importar los proveedores desde el modulo admin
    proveedores=Proveedor.objects.all

    return render(request,'proveedores/proveedores.html', {"proveedores": proveedores})