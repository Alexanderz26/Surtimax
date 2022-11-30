from django.urls import path
from productos.views import categorias, marca, presentacion
from productos.views import productos, productos_crear, productos_editar,presentacion_editar,categorias_eliminar,marca_editar,categorias_editar

urlpatterns = [
    path('',productos,name="productos"),
    path('productos/crear/',productos_crear,name="productos-crear"), 
    path('productos/crear/<int:pk>',productos_editar,name="productos-editar"),
    path('productos/presentacion/<int:pk>',presentacion_editar,name="presentacion-editar"),
    path('productos/marca/<int:pk>',marca_editar,name="marca-editar"),
    path('productos/categorias/<int:pk>',categorias_editar,name="categorias-editar"),




    path('categorias/',categorias,name='categorias'),
    path('categorias/eliminar/<int:pk>/',categorias_eliminar,name='categorias_eliminar'),
    path('marca/',marca,name='marca'),
    path('presentacion/',presentacion,name='presentacion'), 

]
