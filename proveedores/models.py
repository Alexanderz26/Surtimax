from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.

class Proveedor(models.Model):
    razonSocial=models.CharField(max_length=50, verbose_name="Razón Social")
    sectorComercial=models.CharField(max_length=50, verbose_name="Sector Comercial")
    class TipoDocumento(models.TextChoices):
        NIT='NIT', _('NIT')
        RUT='RUT', _('RUT')
        CC='CC', _('Cédula de Ciudadanía')
        CE='CE', _('Cédula de Extranjería')
        OT='Otro', _('Otro Tipo de Documento')
    tipoDocumento=models.CharField(max_length=4, choices=TipoDocumento.choices, default=TipoDocumento.NIT, verbose_name="Tipo de Documento")
    documento=models.CharField(max_length=50,verbose_name="Número de documento")
    direccion=models.CharField(max_length=100,verbose_name="Dirección")
    telefono=models.CharField(max_length=20,verbose_name="Teléfono")
    email=models.CharField(max_length=50,verbose_name="Correo")
    email=models.EmailField(max_length=150, verbose_name='Correo')
    url=models.URLField(max_length=100, verbose_name='URL', blank=True, null=True)

    class Meta:
        verbose_name_plural='provedores'
    

    #funcion para definir como se muestran los elementos en el admin
    def __str__(self)->str:
        return "%s" %(self.razonSocial) 