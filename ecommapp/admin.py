from django.contrib import admin

from ecommapp.models import cupon, estado_pedido, categoria, cliente, producto

class cuponAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descripcion', 'descuento' )

class estado_pedidoAdmin(admin.ModelAdmin):
    list_display = ('descripcion', )

class categoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')

class clienteAdmin(admin.ModelAdmin):
    list_display = ('username', 'nombre', 'email', 'password')

class productoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'categoria', 'igv', 'imagen', 'precio', 'descuento')

admin.site.register(cupon, cuponAdmin)
admin.site.register(estado_pedido, estado_pedidoAdmin)
admin.site.register(categoria, categoriaAdmin)
admin.site.register(cliente, clienteAdmin)
admin.site.register(producto, productoAdmin)