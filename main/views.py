from django.shortcuts import render

def inicioAdmin(request):
   titulo="panel de control"
   context = {  
        'titulo':titulo   
    }
   return render(request,'index.html',context)



