from rest_framework import generics
from .models import Etudiant, Delegue,Utilisateur
from .serializers import UserSerializer, EtudiantSerializer, DelegueSerializer,USerializer,DSerializer,ESerializer


class CreerUtilisateurView(generics.CreateAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = UserSerializer

class CreerEtudiantView(generics.CreateAPIView):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer

class CreerDelegueView(generics.CreateAPIView):
    queryset = Delegue.objects.all()
    serializer_class = DelegueSerializer



class UserListView(generics.ListAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = USerializer

class EtudiantListView(generics.ListAPIView):
    queryset = Etudiant.objects.all()
    serializer_class = ESerializer

class DelegueListView(generics.ListAPIView):
    queryset = Delegue.objects.all()
    serializer_class = DSerializer