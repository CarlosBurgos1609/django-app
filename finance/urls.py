from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("clientes",views.lista_clientes, name='Clientes'),
    path("transacciones",views.lista_transacciones, name='transacciones')
    
]