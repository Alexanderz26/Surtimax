from django.shortcuts import redirect, render
from productos.forms import  ProductoForm,MarcaForm,CategoriaForm,PresentacionForm
from productos.models import Productos,Categoria,Marca,Presentacion
from django.contrib import messages






#create your views here.
#########################PRODUCTOS################################
def productos(request):
    titulo="Productos"
    productos=Productos.objects.all()
    context={
        'titulo':titulo,
        'productos':productos
    }
    return render(request,'productos/productos.html',context)


#########################PRODUCTOS CREAR################################
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

    #########################PRODUCTOS EDITAR################################

def productos_editar(request, pk):
    titulo="Productos - Editar"
    producto=Productos.objects.get(id=pk)
    if request.method == "POST":
        form= ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos')
        else:
            print("Error")
    else:
     form=ProductoForm(instance=producto)
    context={
        'titulo':titulo,
        'form': form
    }
    return render(request,'productos/productos-crear.html',context)
#########################PRODUCTOS ELIMINAR################################
def eliminar(request):
     return render(request,'productos/eliminar.html',context)
    
        
    #########################CATEGORIAS################################
def categorias(request):
    titulo="categorias"
    categorias=Categoria.objects.all()
    print(categorias)
    if request.method == "POST":
        form=CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se agregó la categoria de {request.POST['nombre']} exitosamente!"
            )
            return redirect('categorias')
        else:
             messages.error(
                request,f"Error al agregar {request.POST['nombre']}!"
            )
    else:
     form=CategoriaForm()

    context={
        'titulo':titulo,
        'categorias':categorias,
        'form':form
    }
    return render(request,'productos/categorias.html',context)

     #########################categoria EDITAR################################

def categorias_editar(request, pk):
    titulo="categorias - Editar"
    categorias=Categoria.objects.get(id=pk)
    if request.method == "POST":
        form= CategoriaForm(request.POST, instance=categorias)
        if form.is_valid():
            form.save()
            return redirect('categorias')
        else:
            print("Error")
    else:
     form=CategoriaForm(instance=categorias)
    context={
        'titulo':titulo,
        'form': form
    }
    return render(request,'productos/categorias.html',context)

#########################CATEGORIAS ELIMINAR##################
def categorias_eliminar(request,pk):
    titulo="categorias"

    categoria=Categoria.objects.filter(id=pk).delete()
    messages.success(
         request,f"Se eliminó categoria exitosamente!"
        )
    return redirect('categoria')

    context={
       'titulo':titulo,   
    }

    return render(request,'productos/categorias.html',context)

#########################MARCA################################
def marca(request):
    titulo="marca"
    marca=Marca.objects.all()
    if request.method == "POST":
        form= MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se agregó la marca de {request.POST['nombre']} exitosamente!"
            )
            return redirect('marca')
        else:
            messages.error(
                request,f"Error al agregar {request.POST['nombre']}!"
            )
    else:
     form=MarcaForm()
    context={
        'titulo':titulo,
        'marca':marca,
    }
    return render(request,'productos/marca.html',context)

     #########################MARCA EDITAR################################

def marca_editar(request, pk):
    titulo="marca - Editar"
    marca=Marca.objects.filter(pk=id)
    if request.method == "POST":
        form= MarcaForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            return redirect('marca')
        else:
            print("Error")
    else:
     form=MarcaForm(instance=marca)
    context={
        'titulo':titulo,
        'form': form
    }
    return render(request,'productos/marca.html',context)



    #########################PRESENTACIÓN ################################

def presentacion(request):
    titulo="presentacion"
    presentacion=Presentacion.objects.all()
    if request.method == "POST":
        form=PresentacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se agregó la presentación de {request.POST['nombre']} exitosamente!"
            )
            return redirect('presentacion')
        else:
             messages.error(
                request,f"Error al agregar {request.POST['nombre']}!"
            )
    else:
     form=PresentacionForm()
    context={
        'titulo':titulo,
        'presentacion':presentacion,
        'form':form
    }
    return render(request,'productos/presentacion.html',context)

    #########################PRESENTACIÓN EDITAR################################

def presentacion_editar(request, pk):
    titulo="Presentacion - Editar"
    presentacion=Presentacion.objects.get(id=pk)
    if request.method == "POST":
        form= PresentacionForm(request.POST, instance=presentacion)
        if form.is_valid():
            form.save()
            return redirect('presentacion')
        else:
            print("Error")
    else:
     form=PresentacionForm(instance=presentacion)
    context={
        'titulo':titulo,
        'form': form
    }
    return render(request,'productos/presentacion.html',context)

     #########################PRESENTACIÓN ELIMINAR################################

