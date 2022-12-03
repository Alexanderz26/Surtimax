from django.shortcuts import render

from proveedores.models import Proveedor
# Create your views here.

def proveedores (request):
    #importar los proveedores desde el modulo admin
    proveedores_list=Proveedor.objects.all()

    return render(request,'proveedores/proveedores.html', {"proveedores": proveedores_list})