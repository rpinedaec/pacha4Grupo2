from django.contrib.auth.models import User, Group
from ecommapp.models import cupon, estado_pedido, categoria
from rest_framework import serializers

class CuponSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = cupon
        fields = '__all__'

class Estado_PedidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = estado_pedido
        fields = '__all__'

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = categoria
        fields = '__all__'
