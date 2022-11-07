"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from main.views import  inicio, inicioAdmin
from productos.views import categorias, marca, presentacion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio , name="inicio"),
    path('adm/', inicioAdmin , name="inicio-admin"),
    path('usuarios/', include('usuarios.urls')),
    path('productos/', include('productos.urls')),
    path('productos/categorias',categorias,name='categorias'),
    path('productos/marca',marca,name='marca'),
    path('productos/presentacion',presentacion,name='presentacion'),



   

    

    
]
