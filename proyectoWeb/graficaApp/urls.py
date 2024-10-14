from django.urls import path
from . import views

urlpatterns = [
    path('', views.grafica_beneficios, name='grafica_beneficios'),
]