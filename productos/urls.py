from django.urls import path
from productos.views import categorias, marca, presentacion
from productos.views import productos,productos_editar, productos_crear,presentacion_editar,marca_editar,categorias_editar,categoria_eliminar,marca_eliminar,presentacion_eliminar,productos_eliminar

urlpatterns = [
    ################################ URL PRODUCTOS ####################################
    path('producto/',productos,name="productos"),
    path('productos/crear/',productos_crear,name="productos-crear"), 
    path('productos/crear/<int:pk>',productos_editar,name="productos-editar"),
    path('productos/productos/eliminar/<int:pk>/',productos_eliminar,name="productos-eliminar"),
    ################################ URL PRESENTACIÓN####################################
    path('presentacion/',presentacion,name='presentacion'), 
    path('productos/presentacion/<int:pk>',presentacion_editar,name="presentacion-editar"),
    path('productos/presentacion/eliminar/<int:pk>/',presentacion_eliminar,name="presentacion-eliminar"),
    ################################ URL CATEGORIAS ####################################
    path('categorias/',categorias,name='categorias'),
    path('productos/categorias/<int:pk>',categorias_editar,name="categorias-editar"),
    path('productos/eliminar/<int:pk>/',categoria_eliminar,name="categoria-eliminar"),
    ################################ URL MARCA ####################################
    path('marca/',marca,name='marca'),
    path('productos/marca/<int:pk>',marca_editar,name="marca-editar"),
    path('productos/marca/eliminar/<int:pk>/',marca_eliminar,name="marca-eliminar"),
    

]
