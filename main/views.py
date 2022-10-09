from django.shortcuts import render

def inicioAdmin(request):
    titulo= "inicio"
    nombre="giovany"
    context = {
        'nombres':nombre,
        'titulo': titulo
    }
    return render(request,'index.html',context)