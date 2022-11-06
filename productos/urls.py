from django.urls import path
from main.views import categorias 
from productos.views import productos, productos_crear

urlpatterns = [
    path('',productos,name="productos"),
    path('crear/',productos_crear,name="productos-crear"),
    path('categorias/',categorias,name="Categorias"),


]
