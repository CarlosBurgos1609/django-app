from django.shortcuts import render
from django.http import HttpResponse
from .models import cliente, transaccione

def index(request):
    return HttpResponse(":::Welcom to my site:::")

def lista_clientes(request):
    #return HttpResponse ("Here you find a list of users")
    clientes = cliente.objects.all()
    return render(request, 'finance/clientes.html', {'cliente':clientes})

def lista_transacciones(request):
    #return HttpResponse ("Here you find a list of users")
    transacciones = transaccione.objects.all()
    return render(request, 'finance/transacciones.html', {'transaccione':transacciones})

# def create_user(request):
#     return HttpResponse ("Here you find a list of people")
# # Create your views here.
