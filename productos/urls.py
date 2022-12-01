from django.urls import path
from productos.views import categorias, marca, presentacion
from productos.views import productos, productos_crear, productos_editar,presentacion_editar,marca_editar,categorias_editar,categoria_eliminar,marca_eliminar,presentacion_eliminar

urlpatterns = [
    path('',productos,name="productos"),
    path('productos/crear/',productos_crear,name="productos-crear"), 
    path('productos/crear/<int:pk>',productos_editar,name="productos-editar"),
    path('productos/presentacion/<int:pk>',presentacion_editar,name="presentacion-editar"),
    path('productos/eliminar/<int:pk>/',categoria_eliminar,name="categoria-eliminar"),
    path('productos/marca/eliminar/<int:pk>/',marca_eliminar,name="marca-eliminar"),
    path('productos/presentacion/eliminar/<int:pk>/',presentacion_eliminar,name="presentacion-eliminar"),


    path('productos/marca/<int:pk>',marca_editar,name="marca-editar"),
    path('productos/categorias/<int:pk>',categorias_editar,name="categorias-editar"),
    path('categorias/',categorias,name='categorias'),
    path('marca/',marca,name='marca'),
    path('presentacion/',presentacion,name='presentacion'), 
    

]
