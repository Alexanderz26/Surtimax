from django.shortcuts import redirect, render

from productos.forms import MarcaForm,CategoriaForm, PresentacionForm
from productos.models import Marca,Categoria,Presentacion


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

    
def categorias(request):
    titulo="categorias"

    context={
        'titulo':titulo
    }
    return render(request,'productos/categorias.html',context)
    
def marca(request):
    titulo="marca"
    marca=Marca.objects.all()
    if request.method == "POST":
        form= MarcaForm(request.POST)
        print(request.POST)
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
        'form':form
    }
    return render(request,'productos/marca.html',context)
def categorias(request):
    titulo="categorias"
    categorias=Categoria.objects.all()
    if request.method == "POST":
        form=CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria')
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

def presentacion(request):
    titulo="presentacion"
    presentacion=Presentacion.objects.all()
    if request.method == "POST":
        form=PresentacionForm(request.POST)
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