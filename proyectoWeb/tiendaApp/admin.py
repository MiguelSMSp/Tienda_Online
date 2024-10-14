from django.contrib import admin
from .models import CategoriaProd, Producto, Proveedores

# Register your models here.

class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields =('created', 'updated')


@admin.register(Producto)
class ProductoAdmin (admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre', 'modelo', 'categoria','ubicacion_almacen','cantidad_tienda','cantidad_almacen','cantidad_inicial','precio_tienda','proveedor', 'cantidad_porcentaje', 'pedir_producto')
    change_list_template = "admin/producto_change_list.html"


    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['grafica_url'] = '/grafica_beneficios/'
        return super().changelist_view(request, extra_context=extra_context)

    def pedir_producto(self, obj):
        return (obj.cantidad_tienda + obj.cantidad_almacen) <= obj.cantidad_inicial * 0.10

    pedir_producto.boolean = True

    def cantidad_porcentaje(self, obj):
        # Devuelve la cantidad_porcentual con el símbolo %
        return f"{obj.cantidad_porcentual}%"

    cantidad_porcentaje.short_description = 'Cantidad Porcentual'




class Proveedores_admin(admin.ModelAdmin):
    readonly_fields =('created', 'updated')
    list_display = ('nombre','email', 'facturacion','cif')


admin.site.register(CategoriaProd, CategoriaProdAdmin)
#admin.site.register(Producto, ProductoAdmin)
admin.site.register(Proveedores, Proveedores_admin)