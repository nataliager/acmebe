from rest_framework import serializers
from acmeApp.models.sede import Sede

class SedeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sede
        fields = ['id', 'ciudad', 'direccion','telefono']  

        def to_representation(self, obj):  

            sede = Sede.objects.get(id=obj.id)
            
            return {
                'id': sede.id,
                'ciudad': sede.ciudad,
                'direccion': sede.direccion,
                'telefono': sede.telefono,
            }
