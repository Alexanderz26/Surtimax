from django.shortcuts import render
from django.http import HttpResponseRedirect
from contacto.models import Contacto
from django.contrib import messages
# Create your views here.
def contacto(request):

    return render(request, "contacto.html/")

def add_contacto(request):

    if request.method=="POST":
        if request.POST.get('nombre')\
            and request.POST.get('email')\
            and request.POST.get('motivo') \
            and request.POST.get('comentario')\
            or request.POST.get('respuesta'):
            contacto = Contacto()
            contacto.nombre = request.POST.get('nombre')
            contacto.email = request.POST.get('email')  
            contacto.motivo = request.POST.get('motivo')
            contacto.comentario = request.POST.get('comentario')
            contacto.respuesta = request.POST.get('respuesta')
            contacto.save()
            messages.success(request, "Contacto añadido con éxito!")
            return render("contacto/")
        else:
            return render(request, "contacto.html")    
                 
                   