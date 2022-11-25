from rest_framework import serializers
from acmeApp.models.proveedor import Proveedor

class ProveedorSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Proveedor
        fields = ['id', 'nombre', 'telefono','correo']  

        def to_representation(self, obj):  

            proveedor = Proveedor.objects.get(id=obj.id)
            
            return {
                'id': proveedor.id,
                'nombre': proveedor.nombre,
                'telefono': proveedor.telefono,
                'correo': proveedor.correo,
            }