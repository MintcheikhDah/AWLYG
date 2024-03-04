from django.shortcuts import render
#from django.http import JsonResponse
#from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
#from etudient.models import Etudiant, Delegue 
from fichier.models import Fichier
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Admin
from .serializers import AdminSerializer


@api_view(['GET'])
def get_Admin(request):
        admin=Admin.objects.alll()
        serializer = AdminSerializer(admin,many=False)
        print(admin)
        return Response({"Admin":serializer.data})
def inscription(request):
    # Logique pour l'inscription d'un nouvel admin
    if request.method == 'POST':
        # Traitement de l'inscription
        return Response({'message': 'Inscription réussie'})

def authentification(request):
    # Logique d'authentification de l'admin
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Authentification réussie'})
        else:
            return Response({'message': 'Authentification échouée'})

def creer_etudiant(request):
    # Logique pour la création d'un nouvel étudiant
    if request.method == 'POST':
        # Traitement de la création de l'étudiant
        return Response({'message': 'Étudiant créé avec succès'})

def definir_delegue(request):
    
    if request.method == 'POST':
        
        return Response({'message': 'Délégué défini avec succès'})

def crud_fichier(request):
    
    if request.method == 'GET':
        
        fichiers = Fichier.objects.all()
        
        return Response({'fichiers': fichiers})
    
    elif request.method == 'POST':
        
        return Response({'message': 'Fichier créé avec succès'})
    
    elif request.method == 'PUT':
        
        return Response({'message': 'Fichier mis à jour avec succès'})
    
    elif request.method == 'DELETE':

        return Response({'message': 'Fichier supprimé avec succès'})
