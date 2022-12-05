from django import forms
from productos.models import Productos,Marca,Categoria,Presentacion
   
class ProductoForm(forms.ModelForm):
    class Meta:
        model=Productos
        exclude=["estado"]

class MarcaForm(forms.ModelForm):
    class Meta:
        model= Marca
        exclude=["estado"]

class CategoriaForm(forms.ModelForm):
    class Meta:
        model= Categoria
        exclude=["estado"]

class PresentacionForm(forms.ModelForm):
    class Meta:
        model= Presentacion
        exclude=["estado"]

