from django import forms
from productos.models import Productos,Marca,Categoria,Presentacion
from django_select2 import forms as s2forms


class ProductoWidget(s2forms.ModelSelect2Widget):
    search_fields ={
        "nombre__icontains"
        "id__icontains"

    }
    
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

