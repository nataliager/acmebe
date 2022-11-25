from rest_framework import serializers
from acmeApp.models.user import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from acmeApp.models.sede import Sede
from acmeApp.serializers.sedeSerializer import SedeSerializer

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ['id', 'username','password', 'sede']

        def to_representation(self, obj):

            user = User.objects.get(id=obj.id)
            sede = Sede.objects.get(id=obj.id)

            return {
                    'id': user.id,
                    'username': user.username,
                    'sede': sede.id
                    }
        
class UserUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = User
        fields = ['id', 'username', 'sede']

        def to_representation(self, obj):

            user = User.objects.get(id=obj.id)
            sede = Sede.objects.get(id=obj.id)

            return {
                    'id': user.id,
                    'username': user.username,
                    'sede': sede.id
                    }

class UserSerializerRepresentation(serializers.ModelSerializer):

    sede = SedeSerializer()

    class Meta:
        
        model = User
        fields = ['id', 'username', 'sede']

        def to_representation(self, obj):
            
            user = User.objects.get(id=obj.id)
            sede = Sede.objects.get(id_sede=obj.id)

            return {
                'id': user.id,
                'username': user.username,
                'sede': {
                    'id': sede.id,
                    'ciudad': sede.ciudad,
                    'direccion': sede.direccion,
                    'telefono': sede.telefono,
                    }
                }

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass
