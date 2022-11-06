from django.shortcuts import redirect, render
from productos.forms import ProductoForm
from productos.models import Productos

#create your views here.
def productos(request):
    titulo="Productos"
    productos= Productos.objects.all()
    context={
        'titulo':titulo,
        'productos':productos
    }
    return render(request,'productos/productos.html',context)

def productos_crear(request):
    titulo="Productos - Crear"
    if request.method == "POST":
        form= ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos')
        else:
            print("Error")
    else:
     form=ProductoForm()
    context={
        'titulo':titulo,
        'form': form
    }
    return render(request,'productos/productos-crear.html',context)

def categorias(request):
    titulo="categorias"

    context={
        'titulo':titulo
    }
    return render(request,'productos/categorias.html',context)
   



   






   


