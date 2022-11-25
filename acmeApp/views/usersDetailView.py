from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from acmeApp.models.user import User
from acmeApp.serializers.userSerializer import UserSerializer

class UsersDetailView(APIView):

    permission_classes = [IsAuthenticated]

    #Obtiene todos los usuarios de la BD
    def get(self, request, *args, **kwargs):

        users = User.objects.all().order_by('username')
        serializer = UserSerializer(users,many=True)

        return Response(serializer.data)
