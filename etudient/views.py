from rest_framework import generics
from .models import Etudiant, Delegue
from .serializers import  EtudiantSerializer ,DelegueSerializer,DSerializer,ESerializer
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
#from Knox.auth import AuthToken
#from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate

# inscription l etudiant

class EtudiantInscriptionView(generics.CreateAPIView):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer
    permission_classes = [AllowAny]
    parser_classes = [JSONParser]

# creer delegue
class DelegueCreateView(generics.CreateAPIView):
    queryset = Delegue.objects.all()
    serializer_class = DelegueSerializer
    #permission_classes = [AllowAny]
    parser_classes = [JSONParser]

#listr les users


#lister les etudiants
    
class EtudiantListView(generics.ListAPIView):
    queryset = Etudiant.objects.all()
    serializer_class = ESerializer


#lister les delegues
    
class DelegueListView(generics.ListAPIView):
    queryset = Delegue.objects.all()
    serializer_class = DSerializer


#liste un seul etudiant
class EtudiantListCreateView(generics.ListCreateAPIView):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer

#crud etudiant
class EtudiantRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer

#login


class EtudiantLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user and ( hasattr(user, 'est_etudient')):
            # L'utilisateur est un étudiant et l'authentification est réussie
            return Response({"message": "Authentification réussie pour l'étudiant"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Échec de l'authentification pour l'étudiant"}, status=status.HTTP_401_UNAUTHORIZED)

class DelegueLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user and user.is_delegue:
            # L'utilisateur est un délégué et l'authentification est réussie
            return Response({"message": "Authentification réussie pour le délégué"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Échec de l'authentification pour le délégué"}, status=status.HTTP_401_UNAUTHORIZED)
