from rest_framework.response import Response
from rest_framework.views import APIView
from acmeApp.models.sede import Sede
from acmeApp.serializers.sedeSerializer import SedeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

class SedesDetailView(APIView):

    permission_classes = [IsAuthenticated]

    #Obtiene todas las sedes de la BD
    def get(self, request, *args, **kwargs):

        sedes = Sede.objects.all().order_by('ciudad')
        serializer = SedeSerializer(sedes,many=True)

        return Response(serializer.data)

#Vista concreta para recuperar, actualizar o eliminar una instancia de modelo
class SedeDetailView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated]

    queryset = Sede.objects.all()
    serializer_class = SedeSerializer

    #Todo funciona correctamente



