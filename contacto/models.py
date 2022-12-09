from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Contacto(models.Model):
    nombre=models.CharField(max_length=50, verbose_name='Nombre')
    email=models.EmailField(max_length=50, verbose_name='Correo Electronico')
    class MotivoContacto (models.TextChoices):
        IG = 'IG', _('InformacionGeneral'),
        P = 'P', _('Pedidos')
        C = 'C',_('Comentarios')
        PQR = 'PQR', _('PQRs')
    motivo = models.CharField(max_length=4, choices=MotivoContacto.choices, default=MotivoContacto.C, verbose_name='Motivo de Contacto')
    comentario = models.CharField(max_length=300, verbose_name='Comentarios')
    respuesta = models.BooleanField()

    def __str__(self) -> str:
        return "%s" %(self.nombre)
