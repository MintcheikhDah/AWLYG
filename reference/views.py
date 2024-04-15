#from django.http import JsonResponse
from .models import Niveau, Filiere, Groupe, AnneeUniversitaire
#from rest_framework.decorators import api_view
from rest_framework.response import Response
from .permissions import AdministrateurPermission
from rest_framework import viewsets

from .serializers import NiveauSerializer, FiliereSerializer, GroupeSerializer, AnneeUniversitaireSerializer


class NiveauViewSet(viewsets.ModelViewSet):
    queryset = Niveau.objects.all()
    serializer_class = NiveauSerializer

class FiliereViewSet(viewsets.ModelViewSet):
    queryset = Filiere.objects.all()
    serializer_class = FiliereSerializer

class GroupeViewSet(viewsets.ModelViewSet):
    queryset = Groupe.objects.all()
    serializer_class = GroupeSerializer

class AnneeUniversitaireViewSet(viewsets.ModelViewSet):
    queryset = AnneeUniversitaire.objects.all()
    serializer_class = AnneeUniversitaireSerializer


#les vues pour faire crud

