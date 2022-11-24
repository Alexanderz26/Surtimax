from django.shortcuts import redirect, render




def inicio(request):
    titulo="Inicio"
    context = {  
         'titulo': titulo 
    }
    return render(request,'login.html',context)

def inicioAdmin(request):
    titulo="Panel de control"
    context = {  
        'titulo': titulo   
    }
    return render(request,'index.html',context)

    
    


