from django.urls import path
from usuarios.views import usuarios, usuarios_crear

urlpatterns = [
    path('', usuarios,name="usuarios"),
    path('usuarios-crear/', usuarios_crear,name="usuarios-crear"),
]