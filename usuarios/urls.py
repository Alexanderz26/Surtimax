from django.urls import path

from usuarios.views import usuarios, usuarios_crear, usuarios_editar,usuarios_eliminar

urlpatterns = [
    path('', usuarios,name="usuarios"),
    path('usuarios-crear/', usuarios_crear,name="usuarios-crear"),
    path('usuarios-editar/<int:pk>/',usuarios_editar,name="usuarios-editar"),
    path('usuarios-eliminar/<int:pk>/',usuarios_eliminar,name="usuarios-eliminar"),
]
    