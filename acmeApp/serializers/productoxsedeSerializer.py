from rest_framework import serializers
from acmeApp.models.productoxsede import Productoxsede
from acmeApp.models.producto import Producto
from acmeApp.models.sede import Sede
from acmeApp.serializers.sedeSerializer import SedeSerializer
from acmeApp.serializers.productoSerializer import ProductoSerializer

class ProductoxsedeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Productoxsede
        fields = ['id', 'cantDisponible', 'cantReservada','refProducto','refSede','talla']  

        def to_representation(self, obj):  

            productoxsede = Productoxsede.objects.get(id=obj.id)
            producto = Producto.objects.get(id=obj.id)
            sede = Sede.objects.get(id=obj.id)

            return {
                'id': productoxsede.id,
                'cantDisponible': productoxsede.cantDisponible,
                'cantReservada': productoxsede.cantReservada,
                'refProducto': producto.id,
                'refSede': sede.id,
                'talla': productoxsede.talla,
            }
        
class ProductoxsedeSerializerRepresentation(serializers.ModelSerializer):

    sede = SedeSerializer()
    producto = ProductoSerializer()

    class Meta:

        model = Productoxsede
        fields = ['id', 'cantDisponible', 'cantReservada','refProducto','refSede','talla']  

    def to_representation(self, obj): 

        sede = SedeSerializer()
        producto = ProductoSerializer() 

        productoxsede = Productoxsede.objects.get(id=obj.id)
        producto = Producto.objects.get(id=obj.id)
        sede = Sede.objects.get(id=obj.id)

        return {

            'id': productoxsede.id,
            'cantDisponible': productoxsede.cantDisponible,
            'cantReservada': productoxsede.cantReservada,
            'refProducto':{
                'id': producto.id,
                'tipo': producto.tipo,
                'marca': producto.marca,
                'color': producto.color,
                'descripcion': producto.descripcion
                },
            'refSede': {
                'id': sede.id,
                'ciudad': sede.ciudad,
                'direccion': sede.direccion,
                'telefono': sede.telefono,
                },
            'talla': productoxsede.talla 
            }
