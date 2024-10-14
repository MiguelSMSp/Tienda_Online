from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from pedidosApp.models import Pedido, LineaPedido
from carroApp.carro import Carro

# Create your views here.

@login_required(login_url='/autenticacion/logear')
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    lineas_pedido = []

    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value['cantidad'],
            user=request.user,
            pedido=pedido,
        ))

    LineaPedido.objects.bulk_create(lineas_pedido)

    actualizar_stock(pedido.id)




    messages.success(request, 'Pedido realizado con éxito')
    carro.limpiar_carro()
    return redirect('Tienda')



def actualizar_stock(pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)

    for linea_pedido in pedido.lineapedido_set.all():
        producto = linea_pedido.producto
        cantidad_pedida = linea_pedido.cantidad

        # Primero, resta de la cantidad en almacén
        if producto.cantidad_almacen >= cantidad_pedida:
            producto.cantidad_almacen -= cantidad_pedida
        else:
            cantidad_pedida -= producto.cantidad_almacen
            producto.cantidad_almacen = 0

            # Si el almacen esta a 0 resta la cantidad restante de la cantidad en tienda
            if producto.cantidad_tienda >= cantidad_pedida:
                producto.cantidad_tienda -= cantidad_pedida
            else:
                producto.cantidad_tienda = 0

        # Guardar los cambios en el producto
        producto.save()


