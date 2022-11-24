from django.urls import path
from productos.views import categorias, marca, presentacion
from productos.views import productos, productos_crear, productos_editar, productos_eliminar

urlpatterns = [
    path('',productos,name="productos"),
    path('productos/crear/',productos_crear,name="productos-crear"), 
    path('productos/editar/<int:pk>',productos_editar,name="productos-editar"),
    path('productos/eliminar/<int:pk>',productos_eliminar,name="productos-eliminar"),
    path('categorias/',categorias,name='categorias'),
    path('marca/',marca,name='marca'),
    path('presentacion/',presentacion,name='presentacion'), 

]
