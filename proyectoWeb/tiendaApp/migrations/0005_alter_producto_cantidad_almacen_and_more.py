# Generated by Django 5.0.7 on 2024-07-31 05:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaApp', '0004_producto_ubicacion_almacen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='cantidad_almacen',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='producto',
            name='cantidad_tienda',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]