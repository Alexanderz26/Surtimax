# Generated by Django 4.1.1 on 2022-12-03 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0007_productos_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='descripcion',
            field=models.TextField(max_length=256, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='descripcion',
            field=models.TextField(max_length=1024, verbose_name='Descripción'),
        ),
    ]