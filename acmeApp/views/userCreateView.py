from rest_framework import status, views
from rest_framework.response import Response
from acmeApp.serializers.userSerializer import UserSerializer

class UserCreateView(views.APIView):

    #Metodo para registrar un usuario en la aplicación
    def post(self, request, *args, **kwargs):

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
                'user': {
                    'id' : serializer.data["id"],
                    'username': serializer.data['username'],
                    'sede' : serializer.data['sede']
                },
                "detail" : "Usuario registrado con exito!"
                }, status=status.HTTP_200_OK)
