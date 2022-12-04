from django.shortcuts import render
from django.http import HttpResponseRedirect
from proveedores.models import Proveedor
from django.contrib import messages
# Create your views here.

def proveedores (request):
    
    #importar los proveedores desde el modulo admin
    proveedores_list=Proveedor.objects.all()

    

    return render(request,'proveedores/proveedores.html',  {"proveedores": proveedores_list})

#Function to ADD Proveedor
def add_proveedor(request):
    if request.method=="POST":
        if request.POST.get('razonSocial') \
            and request.POST.get('sectorComercial')\
            and request.POST.get('tipoDocumento') \
            and request.POST.get('documento') \
            and request.POST.get('direccion') \
            and request.POST.get('telefono') \
            and request.POST.get('email') \
            or request.POST.get('url'):
            proveedor= Proveedor()  
            proveedor.razonSocial= request.POST.get('razonSocial')
            proveedor.sectorComercial= request.POST.get('sectorComercial')
            proveedor.tipoDocumento= request.POST.get('tipoDocumento')
            proveedor.documento= request.POST.get('documento')
            proveedor.direccion= request.POST.get('direccion')
            proveedor.telefono= request.POST.get('telefono')
            proveedor.email= request.POST.get('email')
            proveedor.url= request.POST.get('url')
            proveedor.save()
            messages.success(request, "Proveedor añadido con éxito!")
            return HttpResponseRedirect("/")
        else:
            return render (request, 'add.html') ##cambiar cuando sea necesario
#Function to View  Proveedor data individually
def proveedor(request, proveedor_id):
    proveedor = Proveedor.objects.get( id = proveedor_id) 
    if proveedor != None:
        return render(request, "edit.html", {'proveedor':proveedor} )
#Function to EDIT Proveedor
def edit_proveedor(request):
    if request.method == "POST":
        proveedor = Proveedor.objects.get(id = request.POST.get('id'))
        if proveedor != None:
            proveedor.razonSocial= request.POST.get('razonSocial')
            proveedor.sectorComercial= request.POST.get('sectorComercial')
            proveedor.tipoDocumento= request.POST.get('tipoDocumento')
            proveedor.documento= request.POST.get('documento')
            proveedor.direccion= request.POST.get('direccion')
            proveedor.telefono= request.POST.get('telefono')
            proveedor.email= request.POST.get('email')
            proveedor.url= request.POST.get('url')
            proveedor.save()
            messages.success(request, "Proveedor Actualizado con éxito!")
            return HttpResponseRedirect("/")
#Function to DELETE Proveedor
def delete_proveedor(request, proveedor_id):
    proveedor = Proveedor.objects.get(id= proveedor_id)
    proveedor.delete()
    messages.success(request, "Proveedor eliminado satisfactoriamente!")
    return HttpResponseRedirect("/")