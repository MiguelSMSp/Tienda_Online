from django.shortcuts import render
from carroApp.carro import Carro


# Create your views here.

def home(request):

    carro=Carro(request)
    return render (request, 'proyectoWebApp/home.html')


def contacto(request):
    return render(request, 'proyectoWebApp/contacto.html')