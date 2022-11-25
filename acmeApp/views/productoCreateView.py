from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from acmeApp.serializers.productoSerializer import ProductoSerializer
from rest_framework import status

class ProductoCreateView(views.APIView):

    permission_classes = [IsAuthenticated]

    #Crea un producto en la BD 
    def post(self, request, *args, **kwargs): 

        serializer = ProductoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        #Respuesta: codigo de respuesta CREADO e información del producto
        return Response({
                    'producto': serializer.data,
                    "detail" : "Producto registrado exitosamente!"
                }, status=status.HTTP_200_OK)