from django.utils.translation import gettext_lazy as _
from django.db import models

 #Create your models here.


class Marca(models.Model):
        nombre=models.CharField(max_length=45,unique=True, verbose_name="Nombre")
class Estado(models.TextChoices):
        ACTIVO ="1",_('ACTIVO')
        INACTIVO ="0",_('INACTIVO')
estado =models.CharField(max_length=1, choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")


class Categoria(models.Model):
       nombre=models.CharField(max_length=50,unique=True,verbose_name="Nombre")
       descripcion=models.CharField(max_length=256,verbose_name="Descripción")
class Estado(models.TextChoices):
        ACTIVO ="1",_('ACTIVO')
        INACTIVO ="0",_('INACTIVO')
estado =models.CharField(max_length=1, choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")

        


class Presentacion(models.Model):
        nombre=models.CharField(max_length=50,unique=True,verbose_name="Nombre")
        prefijos=models.CharField(max_length=5,verbose_name="Prefijos")
class Estado(models.TextChoices):
        ACTIVO ="1",_('ACTIVO')
        INACTIVO ="0",_('INACTIVO')

estado =models.CharField(max_length=1, choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")



class Productos(models.Model):
     categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE,verbose_name="Categorias")
     marca=models.ForeignKey(Marca,on_delete=models.CASCADE,verbose_name="Marca")
     presentacion=models.ForeignKey(Presentacion,on_delete=models.CASCADE,verbose_name="Presentación")
     codigoBarras=models.CharField(max_length=50,verbose_name="CODBARRAS")
     nombre=models.CharField(max_length=50,verbose_name="Nombre")
     descripcion=models.CharField(max_length=1024,verbose_name="Descripción")
class Estado(models.TextChoices):
        ACTIVO ="1",_('ACTIVO')
        INACTIVO ="0",_('INACTIVO')
estado =models.CharField(max_length=1, choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")

def __str__(self)->str:
  return "%s"%(self.marca)
        