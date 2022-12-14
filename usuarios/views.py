from multiprocessing import context
from django.shortcuts import redirect, render
from usuarios.forms import UsuarioForm, UsuarioUpdateForm
from usuarios.models import Usuario
from django.contrib import messages

### login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required

@login_required(login_url='inicio')
@permission_required('usuarios.view_usuario')

def usuarios_crear(request):
    titulo='Usuarios - Crear'
    
    if request.method == "POST":
        form= UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            if not User.objects.filter(username=request.POST['documento']):
                user = User.objects.create_user('nombres','email@email','pass')
                user.username= request.POST['documento']
                user.first_name= request.POST['nombre']
                user.last_name= request.POST['apellidos']
                user.email= request.POST['email']
                user.password=make_password("@" + request.POST['nombre'][0] + request.POST['apellidos'][0] + request.POST['documento'][-4:])
                user.save()
            else:
                user=User.objects.get(username=request.POST['documento'])
            #####creacion por datos####
            usuario= Usuario.objects.create(
                nombre=request.POST['nombre'],
                apellidos=request.POST['apellidos'],
                foto=form.cleaned_data.get('foto'),
                tipoDocumento=request.POST['tipoDocumento'],
                documento=request.POST['documento'],
                fecha_nacimiento=request.POST['fecha_nacimiento'],
                genero=request.POST['genero'],
                direccion=request.POST['direccion'],
                telefono=request.POST['telefono'],
                email=request.POST['email'],
                rol=request.POST['rol'],
                user=user,
                
            )
            return redirect('usuarios')
 
            
        else:
           form= UsuarioForm(request.POST,request.FILES)
       
    else:
        form= UsuarioForm()
    context={
        'form':form,
        'titulo':titulo

    }
    return render (request,"usuarios/usuarios-crear.html",context)
@login_required
@permission_required('usuarios.views_usuario')

# Filtro usuarios.
def usuarios(request, modal_status='hid'):
    titulo="Usuarios"
    usuarios= Usuario.objects.filter(estado='1')
    
    ###cuerpo del modal ###
    modal_title= ""
    modal_txt= ""
    modal_submit= ""
    #######################
    pk_usuario = ""
    tipo= None
    form_update= None
    form =UsuarioForm()

#####################configuracion modal de eliminar ################################################################

    if request.method == "POST" and 'form-eliminar' in request.POST:
        modal_status= 'show'
        pk_usuario = request.POST['pk']
        usuario= Usuario.objects.get(id=pk_usuario)

        ## Cuerpo del modal ##
        modal_title = f"Eliminar {usuario}"
        modal_txt=f"eliminar el usuario {usuario}"
        modal_submit="Eliminar"
        ##############################

        tipo="eliminar"
##################### configuracion modal de editar ################################################################
    if request.method == "POST" and 'form-editar' in request.POST:
        modal_status= 'show'
        pk_usuario = request.POST['pk']
        usuario= Usuario.objects.get(id=pk_usuario)

        ## Cuerpo del modal ##
        modal_title = f"Editar {usuario}"
        modal_submit="Editar"
        ##############################

        tipo="editar"    
        form_update= UsuarioUpdateForm(instance=usuario)


    if request.method == "POST" and 'modal-confirmar' in request.POST:
##################### configuracion de eliminacion ################################################################

        if request.POST['tipo'] == 'eliminar':
            usuario = Usuario.objects.filter(id = int(request.POST['modal-pk'])).update(
                estado='0'
            )
            messages.success(
                request,f"Se elimin?? el usuario  exitosamente!"
            )
            return redirect('usuarios')
##################### configuracion de edicion ################################################################

        if request.POST['tipo'] == 'editar':
            pk_usuario = request.POST['modal-pk']
            usuario = Usuario.objects.get(id=pk_usuario)
            form_update=UsuarioUpdateForm(request.POST,request.FILES, instance=usuario )
            
            if form_update.is_valid():
                form_update.save()
                messages.success(
                    request,f"Se edit?? el usuario {usuario.nombre} exitosamente!"
                )
                return redirect('usuarios')
    context={
        'titulo': titulo,
        'form': form,
        'usuarios': usuarios,
        'modal_status' :modal_status,
        'modal_submit' :modal_submit,
        'modal_title' :modal_title,
        'modal_txt' :modal_txt,
        'pk': pk_usuario,
        'tipo' : tipo,
        'form_update':form_update


    }
    return render(request, 'usuarios/usuarios.html', context)

# Crear Editar.
# def usuarios_editar(request, pk):
#     titulo="Usuarios - Editar"
#     usuario=Usuario.objects.get(id=pk)
#     if request.method == "POST":
#         form= UsuarioForm(request.POST,instance=usuario)
#         if form.is_valid():
#             form.save()
#             messages.success(
#                 request,f"Se edicto el usuario {request.POST['nombre']} exitosamente!"
#             )
#             return redirect ('usuarios')
#         else:
#             print ("Error al guardar")
#     else:
#         form= UsuarioForm(instance=usuario)    

#     context={
#         'titulo': titulo,
#         'form': form
#     }
#     return render(request, 'usuarios/usuarios-crear.html', context)

# # Crear Eliminar.
# def usuarios_eliminar(request, pk):
#     titulo="Usuarios - Eliminar"
#     usuarios= Usuario.objects.all()

#     Usuario.objects.filter(id=pk).update(
#             estado='0' 
#         )  
    
#     return redirect('usuarios')
    

#     context={
#         'titulo': titulo,
#         'usuarios': usuarios,
#     }
#     return render(request, 'usuarios/usuarios-crear.html', context)