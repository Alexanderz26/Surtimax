
from django.shortcuts import redirect, render
from productos.forms import ProductoForm,MarcaForm,CategoriaForm,PresentacionForm
from productos.models import Productos,Categoria,Marca,Presentacion




#create your views here.
def productos(request):
    titulo="Productos"
    productos=Productos.objects.all()
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

def productos_editar(request, pk):
    titulo="Productos - Editar"
    productos= Productos.objects.get(id=pk)
    if request.method == "POST":
        form= ProductoForm(request.POST, intance=productos)
        if form.is_valid():
            form.save()
            return redirect('productos')
        else:
            print("Error al guardar")
    else:
     form=ProductoForm(instance=productos)
    context={
        'titulo':titulo,
        'form': form
    }
    return render(request,'productos/productos-crear.html',context)

def productos_eliminar(request, pk):
    titulo="Productos - Eliminar"
    productos= Productos.objects.all()

    
    Productos.objects.filter(id=pk).update(
     estado='0'
    )
    return redirect('productos')

    context={
        'productos':productos,
        'titulo':titulo,
    }
    return render(request,'productos/productos.html',context)

def categorias(request):
    titulo="categorias"
    categorias=Categoria.objects.all()
    print(categorias)
    if request.method == "POST":
        form=CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categorias')
        else:
            print("No se puede agregar")
    else:
     form=CategoriaForm()

    context={
        'titulo':titulo,
        'categorias':categorias,
        'form':form
    }
    return render(request,'productos/categorias.html',context)

def marca(request):
    titulo="marca"
    marca=Marca.objects.all()
    if request.method == "POST":
        form= MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('marca')
        else:
            print("No se puede agregar")
    else:
     form=MarcaForm()
    context={
        'titulo':titulo,
        'marca':marca,
    }
    return render(request,'productos/marca.html',context)

def presentacion(request):
    titulo="presentacion"
    presentacion=Presentacion.objects.all()
    if request.method == "POST":
        form=CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('presentacion')
        else:
            print("No se puede agregar")
    else:
     form=PresentacionForm()
    context={
        'titulo':titulo,
        'presentacion':presentacion,
        'form':form
    }
    return render(request,'productos/presentacion.html',context)

   



   






   

