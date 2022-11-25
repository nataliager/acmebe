from rest_framework.response import Response
from rest_framework.views import APIView
from acmeApp.models.producto import Producto
from acmeApp.serializers.productoSerializer import ProductoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

class ProductosDetailView(APIView):

    permission_classes = [IsAuthenticated]

    #Obtiene todos los productos de la BD
    def get(self, request, *args, **kwargs):

        productos = Producto.objects.all().order_by('tipo')
        serializer = ProductoSerializer(productos,many=True)

        return Response(serializer.data)

#Vista concreta para recuperar, actualizar o eliminar una instancia de modelo
class ProductoDetailView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated]

    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
