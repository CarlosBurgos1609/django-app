from django.db import models
from django.contrib.auth.hashers import make_password
import datetime

# Create your models here.
class DateTimeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        abstract = True

class cliente(DateTimeModel):
    id_cliente = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=250)
    email = models.EmailField(max_length=50, unique=True, blank=False, null=False)
    phone = models.CharField(max_length=50, blank=False, null=False)
    
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(cliente, self).save(*args, **kwargs)
    
    
class producto(DateTimeModel):
    id_product = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    nombre_product = models.CharField(max_length=50, blank=False, null=False)
    abrebiation = models.CharField(max_length=5, blank=False, null=False)
    description = models.CharField(max_length=100, blank=False, null=False)
    
class cliente_producto(DateTimeModel):
    id_clientes_producto = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    id_cliente = models.ForeignKey(cliente, on_delete=models.CASCADE, blank=False, null=False)
    id_product = models.ForeignKey(producto, on_delete=models.CASCADE, blank=False, null=False)
    numero_cuenta = models.CharField(max_length=50, blank=False, null=False) 
    
class tipos_transaccione(DateTimeModel):
    id_tipos = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    abrebiation = models.CharField(max_length=5, blank=False, null=False)
    description = models.CharField(max_length=100, blank=False, null=False)

class transaccione(DateTimeModel):
    id_transacciones = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    id_clientes_producto = models.ForeignKey(cliente_producto, on_delete=models.CASCADE, blank=False, null=False)
    monto = models.CharField(max_length=11, blank=False, null=False)
    id_tipo_transacción = models.ForeignKey(tipos_transaccione, on_delete=models.CASCADE, blank=False, null=False)