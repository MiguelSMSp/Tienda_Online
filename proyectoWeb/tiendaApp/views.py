import base64
from django.db.models import Sum, Q
from django.shortcuts import render, get_object_or_404
from matplotlib import pyplot as plt
import pandas as pd
import io
from pedidosApp.models import Producto
from pedidosApp.models import LineaPedido


# Create your views here.

def tienda(request):
    productos = Producto.objects.all()  # Una variable que contiene todos nuestros productos y poderlo renderizar en la línea siguiente

    # Obtener datos de productos vendidos y convertirlos en un DataFrame
    productos_vendidos = LineaPedido.objects.values('producto__nombre', 'producto__modelo') \
                             .annotate(total_vendido=Sum('cantidad')) \
                             .order_by('-total_vendido')[:10]
    df = pd.DataFrame(productos_vendidos)

    # Preparar datos para el gráfico
    df['label'] = df.apply(lambda row: f"{row['producto__nombre']} ({row['producto__modelo']})", axis=1)
    labels = df['label']
    sizes = df['total_vendido']

    # Crear gráfico de pastel
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')

    # Convertir el gráfico a un formato que Django pueda manejar
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read()).decode('utf-8')
    uri = 'data:image/png;base64,' + string

    return render(request, 'tiendaApp/tienda.html', {'productos': productos, 'grafico': uri})


def buscar(request):
    query = request.GET.get('q', '')
    if query:
        productos = Producto.objects.filter(
            Q(nombre__icontains=query) | Q(modelo__icontains=query)
        )
    else:
        productos = Producto.objects.all()

    # Obtener datos de productos vendidos y convertirlos en un DataFrame
    productos_vendidos = LineaPedido.objects.values('producto__nombre', 'producto__modelo') \
                             .annotate(total_vendido=Sum('cantidad')) \
                             .order_by('-total_vendido')[:10]
    df = pd.DataFrame(productos_vendidos)

    # Preparar datos para el gráfico
    df['label'] = df.apply(lambda row: f"{row['producto__nombre']} ({row['producto__modelo']})", axis=1)
    labels = df['label']
    sizes = df['total_vendido']

    # Crear gráfico de pastel
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')

    # Convertir el gráfico a un formato que Django pueda manejar
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read()).decode('utf-8')
    uri = 'data:image/png;base64,' + string

    return render(request, 'tiendaApp/tienda.html', {'productos': productos, 'grafico': uri})



def producto_detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'tiendaApp/producto_detalle.html', {'producto': producto})

