# Generated by Django 4.1.1 on 2022-12-03 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razonSocial', models.CharField(max_length=50, verbose_name='Razon Social')),
                ('sectorComercial', models.CharField(max_length=50, verbose_name='Sector Comercial')),
                ('tipoDocumento', models.CharField(choices=[('NIT', 'NIT'), ('RUT', 'RUT'), ('CC', 'Cédula de Ciudadanía'), ('CE', 'Cédula de Extranjería'), ('Otro', 'Otro Tipo de Documento')], default='NIT', max_length=4, verbose_name='Tipo de Documento')),
                ('documento', models.CharField(max_length=50, verbose_name='Número de documento')),
                ('direccion', models.CharField(max_length=100, verbose_name='Dirección')),
                ('telefono', models.CharField(max_length=20, verbose_name='Teléfono')),
                ('email', models.EmailField(max_length=150, verbose_name='Correo')),
                ('url', models.URLField(max_length=100, verbose_name='URL')),
            ],
        ),
    ]