from django.contrib import admin
from proveedores.models import Proveedor

# Register your models here.

#agrega las funcionalidades de vista y buscador
class ProveedorAdmin (admin.ModelAdmin):
    list_display=("razonSocial", "tipoDocumento", "documento", "sectorComercial", "email")
    search_fields=("razonSocial", "documento")
    list_filter=("sectorComercial",)

#registar el modelo
admin.site.register(Proveedor, ProveedorAdmin)
