from django.contrib import admin
from proveedores.models import Proveedor

# Register your models here.

#agrega las funcionalidades de vista y buscador
class ProveedorAdmin (admin.ModelAdmin):
    list_display=("id", "razonSocial", "tipoDocumento", "documento", "sectorComercial", "email")
    search_fields=("razonSocial", "documento")
    list_filter=("sectorComercial",)
    list_per_page = 8

#registar el modelo
admin.site.register(Proveedor, ProveedorAdmin)
