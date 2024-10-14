from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class Proveedores(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.EmailField (max_length=100)
    facturacion = models.CharField(max_length=100)
    cif = models.CharField (max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Metal:
        verbosa_name = 'proveedor'
        verbose_name_plural = 'proveedores'


class CategoriaProd (models.Model):
    nombre = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True) #para saber cuando se crea
    updated = models.DateTimeField(auto_now_add=True) #para saber cuando se actualiza

    class Meta:
        verbose_name = 'categoriaProd'
        verbose_name_plural = 'categoriasProd'

    def __str__(self):
        return self.nombre



class Producto (models.Model):
    nombre = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ubicacion_almacen = models.CharField(max_length=50)
    categoria = models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True, null=True)
    sn = models.CharField(max_length= 50, blank=True, null=True)
    cantidad_tienda = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    cantidad_almacen = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    cantidad_inicial = models.IntegerField(default=0, validators=[MinValueValidator(0)]) #minvaluevalidator impide que haya numero negativos
    cantidad_porcentual = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)]) #maxvaluevalidator impide que haya un numero mayor a 100
    precio_tienda = models.FloatField()
    precio_sin_iva = models.FloatField() #precio del proveedor sin iva
    precio_con_iva = models.FloatField() #precio proveedor con iva
    iva = models.FloatField()
    descuento = models.FloatField()
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    imagen = models.ImageField(blank=True, null=True, upload_to='tienda')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)



    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.calculo_porcentaje()  # Calcula el porcentaje antes de guardar
        super().save(*args, **kwargs)

    def calculo_porcentaje(self, *args, **kwargs):
        if self.cantidad_inicial > 0:
            self.cantidad_porcentual = ((self.cantidad_tienda + self.cantidad_almacen) / self.cantidad_inicial) * 100
            super().save(*args, **kwargs)

    def umbral_producto(self):
        umbral = self.cantidad_inicial * 0.10
        return (self.cantidad_tienda + self.cantidad_almacen) <= umbral




