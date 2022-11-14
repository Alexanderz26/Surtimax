from multiprocessing import context

from django.shortcuts import redirect, render

from usuarios.forms import UsuarioForm
from usuarios.models import Usuario


# Create your views here.
def usuarios (request):
    titulo="Ver Usuarios"
    usuarios= Usuario.objects.all()
    context={
        'titulo': titulo,
        'usuarios': usuarios
    }
    return render(request, 'usuarios/usuarios.html', context)
# Crear usuarios.
def usuarios_crear(request):
    titulo="Usuarios - Crear"
    if request.method == "POST":
        form= UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('usuarios')
        else:
            print ("Error")
    else:
        form= UsuarioForm()    

    context={
        'titulo': titulo,
        'form': form
    }
    return render(request, 'usuarios/usuarios-crear.html', context)

# Crear Editar.
def usuarios_editar(request, pk):
    titulo="Usuarios - Editar"
    usuario=Usuario.objects.get(id=pk)
    if request.method == "POST":
        form= UsuarioForm(request.POST,instance=usuario)
        if form.is_valid():
            form.save()
            return redirect ('usuarios')
        else:
            print ("Error al guardar")
    else:
        form= UsuarioForm(instance=usuario)    

    context={
        'titulo': titulo,
        'form': form
    }
    return render(request, 'usuarios/usuarios-crear.html', context)

# Crear Eliminar.
def usuarios_eliminar(request, pk):
    titulo="Usuarios - Eliminar"
    usuarios= Usuario.objects.all()

    Usuario.objects.filter(id=pk).update(
            estado='0'
        )  
    return redirect('usuarios')

    context={
        'titulo': titulo,
        'usuarios': usuarios,
    }
    return render(request, 'usuarios/usuarios-crear.html', context)