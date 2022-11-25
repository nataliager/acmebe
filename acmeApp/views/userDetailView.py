from rest_framework import status, views, generics
from django.conf import settings
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from acmeApp.serializers.userSerializer import  UserSerializer, UserSerializerRepresentation
from acmeApp.models.user import User

#Clase que permite hacer el CRUD del usuario logueado
class LogUserDetailView(views.APIView):

    permission_classes = (IsAuthenticated,)

    # Permite al usuario logueado ver sus datos
    def get(self, request, *args, **kwargs):

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        serializer = UserSerializerRepresentation()
        u = User(id=valid_data["user_id"])
        

        result = serializer.to_representation(u)

        return Response(result, status=status.HTTP_200_OK)

    # Permite actualizar los datos de un usuario logueado
    def put(self, request, *args, **kwargs):

        # Decodificacion del token
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        request.data["id"] = valid_data["user_id"] 
        user = User(id=valid_data["user_id"])  

        # Actualizar el usuario autenticado
        serializer = UserSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True) 
        updatedUser = serializer.save()  
        result = serializer.to_representation(updatedUser)  

        return Response(result, status=status.HTTP_200_OK)

    # Permite eliminar el usuario logueado
    def delete(self, request, *args, **kwargs):

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        request.data["id"] = valid_data["user_id"] 
        u = User(id=valid_data["user_id"]) 
        u.delete()

        return Response({"detail": "El usuario fue eliminado exitosamente"}, status=status.HTTP_204_NO_CONTENT)

#Vista concreta para recuperar, actualizar o eliminar una instancia de modelo
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializerRepresentation

#Clase para actualizar usuario con serializador que no retorna contraseña
class UserUpdateView(generics.UpdateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
