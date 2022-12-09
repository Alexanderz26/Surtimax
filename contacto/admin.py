from django.contrib import admin
from .models import Contacto

# Register your models here.
class ContactoAdmin(admin.ModelAdmin):
    list_display=('nombre','email', 'motivo', 'comentario', 'respuesta')
    search_fields=("nombre", "motivo")
    list_filter=("motivo", "respuesta")

admin.site.register(Contacto,ContactoAdmin)