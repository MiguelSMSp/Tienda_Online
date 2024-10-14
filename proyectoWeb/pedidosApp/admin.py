from django.contrib import admin
from . models import Pedido, LineaPedido

# Register your models here.



class Pedido_admin(admin.ModelAdmin):
    list_display = ('id','user',)


admin.site.register(Pedido,Pedido_admin)
admin.site.register(LineaPedido)
