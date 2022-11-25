from rest_framework import serializers
from acmeApp.models.producto import Producto

class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = ['id', 'tipo', 'marca','color', 'descripcion']  

        def to_representation(self, obj):  

            producto = Producto.objects.get(id=obj.id)
            
            return {
                'id': producto.id,
                'tipo': producto.tipo,
                'marca': producto.marca,
                'color': producto.color,
                'descripcion': producto.descripcion
            }