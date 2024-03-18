
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from .serializers import AuthSerializer ,ProfileSerializer


class LoginView(APIView):
    def post(self, request):
        serializer = AuthSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(request, username=serializer.validated_data['username'], password=serializer.validated_data['password'])
            if user is not None:
                login(request, user)
                return Response({'message': 'Authentification réussie'})
        return Response({'message': 'Identifiants incorrects'}, status=400)

# Vue de modification de profil
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            
            return Response({'message': 'Profil modifié avec succès'})
        return Response(serializer.errors, status=400)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({'message': 'Déconnexion réussie'})


