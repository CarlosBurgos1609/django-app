from django.contrib import admin
from .models import cliente, producto, cliente_producto, tipos_transaccione, transaccione

class clientField(admin.ModelAdmin):
    list_display = ('id_cliente', 'email', 'nombre','phone')
        
class productoField(admin.ModelAdmin):
    list_display = ('id_product','nombre_product', 'abrebiation', 'description')
    
class cliente_productoField(admin.ModelAdmin):
    list_display = ('id_clientes_producto','id_cliente', 'id_product', 'numero_cuenta')
    
class tipos_transaccioneField(admin.ModelAdmin):
    list_display = ('id_tipos','nombre', 'abrebiation', 'description')
    
class transaccioneField(admin.ModelAdmin):
    list_display = ('id_transacciones','id_clientes_producto', 'monto', 'id_tipo_transacción')
    

admin.site.register(cliente,clientField )
admin.site.register(producto,productoField)
admin.site.register(cliente_producto,cliente_productoField)
admin.site.register(tipos_transaccione,tipos_transaccioneField)
admin.site.register(transaccione,transaccioneField)

# Register your models here.
