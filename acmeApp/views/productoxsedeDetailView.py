from rest_framework.response import Response
from rest_framework.views import APIView
from acmeApp.models.productoxsede import Productoxsede
from acmeApp.serializers.productoxsedeSerializer import ProductoxsedeSerializer, ProductoxsedeSerializerRepresentation
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

class ProductosxsedeDetailView(APIView):

    permission_classes = [IsAuthenticated]

    #Obtiene todos los productos x sede de la BD
    def get(self, request, *args, **kwargs):

        productosxsede = Productoxsede.objects.all().order_by('talla')
        serializer =ProductoxsedeSerializerRepresentation(productosxsede,many=True)

        return Response(serializer.data)

#Vista concreta para recuperar, actualizar o eliminar una instancia de modelo
class ProductoxsedeDetailView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated]

    queryset = Productoxsede.objects.all()
    serializer_class = ProductoxsedeSerializer


class ProductoxsedeView(generics.RetrieveAPIView):

    queryset = Productoxsede.objects.all()
    serializer_class = ProductoxsedeSerializerRepresentation