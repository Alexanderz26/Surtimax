from django import forms
from productos.models import Productos


class ProductoForm(forms.ModelForm):
    class Meta:
        model=Productos
        fields='__all__'