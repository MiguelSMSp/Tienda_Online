# Generated by Django 5.0.7 on 2024-07-31 03:09

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'categoriaProd',
                'verbose_name_plural': 'categoriasProd',
            },
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('facturacion', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('sn', models.CharField(blank=True, max_length=50, null=True)),
                ('cantidad', models.IntegerField(default=0)),
                ('cantidad_porcentual', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('precio_tienda', models.FloatField()),
                ('precio_sin_iva', models.FloatField()),
                ('precio_con_iva', models.FloatField()),
                ('iva', models.FloatField()),
                ('descuento', models.FloatField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='tienda')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiendaApp.categoriaprod')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiendaApp.proveedores')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['id'],
            },
        ),
    ]