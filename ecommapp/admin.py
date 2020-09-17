from django.contrib import admin

from ecommapp.models import cupon, estado_pedido, categoria

class cuponAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descripcion', 'descuento' )

class estado_pedidoAdmin(admin.ModelAdmin):
    list_display = ('descripcion', )

class categoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')

admin.site.register(cupon, cuponAdmin)
admin.site.register(estado_pedido, estado_pedidoAdmin)
admin.site.register(categoria, categoriaAdmin)