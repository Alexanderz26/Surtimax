from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# ENUM"CC", "CE", "PASAPORTE"
# ENUM"Administrador", "Empleado", "Cliente", "Proveedor"
# ENUM"Activo", "Inactivo"
class Usuario(models.Model):
    nombre=models.CharField(max_length=45, verbose_name="Nombre")
    apellidos=models.CharField(max_length=45, verbose_name="Apellidos")
    foto=models.ImageField(upload_to='images/usuarios',blank=True, default='images/usuarios/default.jpg')
    class TipoDocumento(models.TextChoices):
        CC='CC', _('Cédula de Ciudadanía')
        CE='CE', _('Cédula de Extranjería')
        OT='Otro', _('Otro Tipo de Documento')
    tipoDocumento=models.CharField(max_length=4, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de Documento")
    documento=models.CharField(max_length=50,verbose_name="Número de documento")
    fecha_nacimiento=models.DateField(verbose_name="Fecha de nacimiento", help_text=u"MM/DD/AAAA")
    class Genero(models.TextChoices):
        F='F', _('Femenino')
        M='M', _('Masculino')     
    genero=models.CharField(max_length=2, choices=Genero.choices, default=Genero.F, verbose_name="Tipo de Genero")
    direccion=models.CharField(max_length=100,verbose_name="Dirección")
    telefono=models.CharField(max_length=20,verbose_name="Teléfono")
    email=models.CharField(max_length=50,verbose_name="Correo")
    email= models.EmailField(max_length=150, verbose_name='Correo')
    class Rol(models.TextChoices):
        Administrador='Administrador', _('Administrador')
        Empleado='Empleado', _('Empleado')     
        Cliente='Cliente', _('Cliente')  
        Proveedor='Proveedor', _('Proveedor')  
    rol=models.CharField(max_length=13, choices=Rol.choices, default=Rol.Empleado, verbose_name="Rol")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')     
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    user=models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self)->str:
        return "%s %s" %(self.nombre, self.apellidos)  