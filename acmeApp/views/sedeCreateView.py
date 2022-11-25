from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from acmeApp.serializers.sedeSerializer import SedeSerializer
from rest_framework import status

class SedeCreateView(views.APIView):

    permission_classes = [IsAuthenticated]

    #Crea una sede en la BD 
    def post(self, request, *args, **kwargs): 

        serializer = SedeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        #Respuesta: codigo de respuesta CREADO e información de la sede
        return Response({
                    'sede': serializer.data,
                    "detail" : "Sede registrada exitosamente!"
                }, status=status.HTTP_200_OK)
