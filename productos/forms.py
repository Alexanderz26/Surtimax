from django import forms
from productos.models import Productos,Marca,Categoria,Presentacion


class ProductoForm(forms.ModelForm):
    class Meta:
        model=Productos
        fields='__all__'

class MarcaForm(forms.ModelForm):
    class Meta:
        model= Marca
        fields='__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model= Categoria
        fields='__all__'

class PresentacionForm(forms.ModelForm):
    class Meta:
        model= Presentacion
        fields='__all__'