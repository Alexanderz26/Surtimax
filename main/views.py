from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.defaults import page_not_found
#from django.contrib import messages
#from django.contrib.auth import logout

#####elimina para logic####

# def inicio(request):
#     titulo="Inicio"
#     context = {  
#          'titulo': titulo 
#     }
#     return render(request,'login.html',context)

def inicioAdmin(request):
    titulo="Panel de control"
    context= {  
        'titulo': titulo   
    }
    return render(request,'index.html', context)

def error_404(request,exception):
    return page_not_found(request, '404.html')

def loggedIn(request):
     if request.user.is_authenticated:
         respuesta: "Ingresado como "+ request.user.username
            
     else:
         respuesta:"No estas autenticado."
     return HttpResponse(respuesta)

def logout_user(request):
   # logout(request)
    return redirect("registration/login.html")

def proveedores (request):
    return render(request,'proveedores/proveedores.html')

def compras(request):
    return render (request, 'compras/compras.html')