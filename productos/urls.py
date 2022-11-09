from django.urls import path
from productos.views import productos, productos_crear

urlpatterns = [
    path('',productos,name="productos"),
    path('productos/crear/',productos_crear,name="productos-crear")   

]
