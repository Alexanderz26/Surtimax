from django.utils.translation import gettext_lazy as _
from django.db import models
from proveedores.models import Proveedor
from usuarios.models import Usuario

# Create your models here.

class Compra(models.Model):
    provedor=models.ForeignKey(Proveedor, null=True, blank=True, on_delete=models.CASCADE)
    usuario=models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
    class TipoComprobante(models.TextChoices):
        CF='CF', _('Comprobante Factura')
        NC='NC', _('Nota Crédito')
    tipoComprobante=models.CharField(max_length=50, choices=TipoComprobante.choices, default=TipoComprobante.CF, verbose_name="Tipo de Comprobante")
    fechaIngreso=models.DateField(verbose_name="Fecha de Ingreso", help_text=u"MM/DD/AAAA")

