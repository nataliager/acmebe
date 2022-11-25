from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from acmeApp.serializers.proveedorSerializer import ProveedorSerializer
from rest_framework import status

class ProveedorCreateView(views.APIView):

    permission_classes = [IsAuthenticated]

    #Crea un proveedor en la BD 
    def post(self, request, *args, **kwargs): 

        serializer = ProveedorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        #Respuesta: codigo de respuesta CREADO e información del proveedor
        return Response({
                    'proveedor': serializer.data,
                    "detail" : "Proveedor registrado exitosamente!"
                }, status=status.HTTP_200_OK)