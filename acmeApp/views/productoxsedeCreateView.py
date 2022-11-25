from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from acmeApp.serializers.productoxsedeSerializer import ProductoxsedeSerializer
from rest_framework import status

class ProductoxsedeCreateView(views.APIView):

    permission_classes = [IsAuthenticated]

    #Crea un producto en una sede en la BD 
    def post(self, request, *args, **kwargs): 

        serializer = ProductoxsedeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        #Respuesta: codigo de respuesta CREADO e información del producto en la sede
        return Response({
                    'productoxsede': serializer.data,
                    "detail" : "Producto agregado a la sede exitosamente!"
                }, status=status.HTTP_200_OK)