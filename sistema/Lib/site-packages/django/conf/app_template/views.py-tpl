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
    titulo="productos"
    productos=Productos.objects.all()
    print(productos)
    if request.method == "POST":
        form=ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se agregó el producto de {request.POST['nombre']} exitosamente!"
            )
            return redirect('productos')
        else:
             messages.error(
                request,f"Error al agregar {request.POST['nombre']}!"
            )
    else:
     form=ProductoForm()

    context={
        'titulo':titulo,
        'productos':productos,
        'form':form
    }
    return render(request,'productos/productos-crear.html',context)


   #########################PRODUCTOS EDITAR################################

def productos_editar(request, pk):
    titulo="Productos - Editar"
    productos=Productos.objects.get(id=pk)
    if request.method == "POST":
        form= ProductoForm(request.POST, instance=productos)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se edito el producto{request.POST['nombre']} exitosamente!"
            )
            return redirect('productos')
        else:
            print("Error")
    else:
        form=ProductoForm(instance=productos)
    context={
            'titulo':titulo,
            'form': form
    }
    return render(request,'productos/productos-crear.html',context)

    #########################PRODUCTO ELIMINAR##################
def productos_eliminar(request,pk):
    titulo="productos"
    
    productos=Productos.objects.filter(id=pk).delete()
    messages.success(
            request,f"Se eliminó el producto exitosamente!"
        )
    return redirect('productos')
    
    context={
            'titulo':titulo,
        
    }
    return render(request,'productos/productos.html',context)

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

     #########################CATEGORIAS EDITAR################################

def categorias_editar(request, pk):
    titulo="categorias - Editar"
    categorias=Categoria.objects.get(id=pk)
    if request.method == "POST":
        form= CategoriaForm(request.POST, instance=categorias)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se edito la categoria de {request.POST['nombre']} exitosamente!"
            )
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
def categoria_eliminar(request,pk):
    titulo="Departamentos"
    
    categorias=Categoria.objects.filter(id=pk).delete()
    messages.success(
            request,f"Se eliminó la categoria exitosamente!"
        )
    return redirect('categorias')
    
    context={
        'titulo':titulo,
        
    }
    return render(request,'productos/categoria.html',context)
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
    marca=Marca.objects.get(id=pk)
    if request.method == "POST":
        form= MarcaForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se edito la marca de {request.POST['nombre']} exitosamente!"
            )
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

    ######################### MARCA ELIMINAR##################
def marca_eliminar(request,pk):
    titulo="marca"
    
    marca=Marca.objects.filter(id=pk).delete()
    messages.success(
            request,f"Se eliminó la marca exitosamente!"
        )
    return redirect('marca')
    
    context={
        'titulo':titulo,
        
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
            messages.success(
                request,f"Se edito la presentación de {request.POST['nombre']} exitosamente!"
            )
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

         ######################### PRESENTACIÓN ELIMINAR##################
def presentacion_eliminar(request,pk):
    titulo="presentacion"
    
    presentacion=Presentacion.objects.filter(id=pk).delete()
    messages.success(
            request,f"Se eliminó la presentacion exitosamente!"
        )
    return redirect('presentacion')
    
    context={
        'titulo':titulo,
        
    }
    return render(request,'productos/presentacion.html',context)


