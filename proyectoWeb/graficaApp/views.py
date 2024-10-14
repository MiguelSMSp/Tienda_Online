import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import io
from django.http import HttpResponse
from tiendaApp.models import Producto

# Create your views here.

def grafica_beneficios(request):
    productos = Producto.objects.all()

    df = pd.DataFrame({
        'nombre': [producto.nombre for producto in productos],
        'modelo': [producto.modelo for producto in productos],
        'precio_con_iva': [producto.precio_con_iva for producto in productos],
        'precio_tienda': [producto.precio_tienda for producto in productos],
        'beneficio': [producto.precio_tienda - producto.precio_con_iva for producto in productos]
    })

    datos = {
        'producto proveedor (con IVA) €': df['precio_con_iva'].tolist(),
        'precio en tienda €': df['precio_tienda'].tolist(),
        'beneficio €': df['beneficio'].tolist()
    }

    num_productos = len(df)
    num_datos = len(datos)
    width = 4  # Ancho de las barras
    spacing = 10  # Espacio entre grupos de barras

    x = pd.Series(range(num_productos)) * (width + spacing)

    buf = io.BytesIO()
    fig, ax = plt.subplots(figsize=(18, 8))

    for i, (key, value) in enumerate(datos.items()):
        offset = width * i  # Desplazamiento para cada conjunto de barras
        rects = ax.bar(x + offset, value, width, label=key)
        ax.bar_label(rects, padding=3)

    ax.set_xticks(x + width * (num_datos - 1) / 2)
    ax.set_xticklabels([f"({nombre}-{modelo})" for nombre, modelo in zip(df['nombre'], df['modelo'])], rotation=90)

    ax.set_ylabel('Euros')
    ax.set_title('Beneficios compra-venta')
    ax.legend(loc='upper left', ncols=3)
    ax.set_ylim(0, 2000)
    ax.set_yticks(range(0, 2001, 100))

    plt.tight_layout(pad=2.0)

    plt.savefig(buf, format='png')
    plt.close()

    response = HttpResponse(buf.getvalue(), content_type='image/png')
    return response
