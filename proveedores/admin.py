from django.contrib import admin
from proveedores.models import Proveedor

# Register your models here.

class ProveedorAdmin (admin.ModelAdmin):
    list_display=("razonSocial", "tipoDocumento", "documento")
    search_fields=("razonSocial", "documento")

admin.site.register(Proveedor, ProveedorAdmin)
