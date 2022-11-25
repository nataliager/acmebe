from rest_framework.response import Response
from rest_framework.views import APIView
from acmeApp.models.proveedor import Proveedor
from acmeApp.serializers.proveedorSerializer import ProveedorSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

class ProveedoresDetailView(APIView):

    permission_classes = [IsAuthenticated]

    #Obtiene todos los proveedores de la BD
    def get(self, request, *args, **kwargs):

        provedores = Proveedor.objects.all().order_by('nombre')
        serializer = ProveedorSerializer(provedores,many=True)

        return Response(serializer.data)

#Vista concreta para recuperar, actualizar o eliminar una instancia de modelo
class ProveedorDetailView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated]

    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
