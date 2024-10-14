from django.urls import path
from . import views

urlpatterns = [
    path('',views.tienda, name='Tienda'),
    path('buscar/', views.buscar, name='buscar'),
    path('producto/<int:producto_id>/', views.producto_detalle, name='producto_detalle'),
]


