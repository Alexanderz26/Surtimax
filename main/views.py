from django.shortcuts import render, redirect
from django.views.defaults import page_not_found
#from django.contrib import messages
#from django.contrib.auth import logout
from django.contrib.auth import logout

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

def reportes_informe(request):
    titulo="Reportes"
    context= {  
        'titulo': titulo   
    }
    return render(request,'reportes.html', context)

#def loggedIn(request):
#    if request.user.is_authenticated:
#         respuesta: "Ingresado como "+ request.user.username
            
#     else:
#         respuesta:"No estas autenticado."
#     return HttpResponse(respuesta)
###################### login ################
def logout_user(request):
    logout(request)
    return redirect("inicio")
