from rest_framework import generics
from .models import Administrateur
from rest_framework import status
from rest_framework.response import Response
from .serializers import AdministrateurSerializer,AdministrateurSerializer1
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AdministrateurLoginSerializer
from django.contrib.auth.models import User



#creer un admin
class AdministrateurCreateView(generics.CreateAPIView):
    queryset = Administrateur.objects.all()
    serializer_class = AdministrateurSerializer1

    def create(self, request, *args, **kwargs):
        
        if Administrateur.objects.count() > 0:
            return Response('Administrateur already exists', status=status.HTTP_409_CONFLICT)
        return super().create(request, *args, **kwargs)
    





#deconnexion
class AdministrateurLogoutView(generics.DestroyAPIView):
    queryset = Token.objects.all()

    def post(self, request, *args, **kwargs):
        token = self.get_object()

        if token.user == request.user:
            token.delete()

            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_403_FORBIDDEN)

#modifier le profile
class AdministrateurUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Administrateur.objects.all()
    serializer_class = AdministrateurSerializer

    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

#login



class AdministrateurLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = AdministrateurLoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data['user']
            # Vous pouvez ajouter ici toute logique supplémentaire après l'authentification
            return Response("Authenticated successfully", status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
