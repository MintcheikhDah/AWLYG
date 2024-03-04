
from .models import Etudiant, Delegue
from fichier.models import Fichier

from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import  Etudiant
from fichier.models import Fichier
from django.db.models.signals import pre_save
from django.dispatch import receiver


def etudiant_view(request):
    etudiants = Etudiant.objects.all()
    return render(request,  {'etudiants': etudiants})

def delegue_view(request):
    delegues = Delegue.objects.all()
    return render(request,  {'delegues': delegues})


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from fichier.models import Fichier
import json


@csrf_exempt
def fichier_list(request):
    if request.method == 'GET':
        fichiers = Fichier.objects.filter(niveau=request.user.niveau, filiere=request.user.filiere, groupe=request.user.groupe)
        data = [{'nom': fichier.nom, 'niveau': fichier.niveau, 'filiere': fichier.filiere, 'groupe': fichier.groupe} for fichier in fichiers]
        return JsonResponse(data, safe=False)
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        fichier = Fichier.objects.create(nom=data['nom'], niveau=request.user.niveau, filiere=request.user.filiere, groupe=request.user.groupe)
        return JsonResponse({'message': 'Fichier créé avec succès'}, status=201)
    
@csrf_exempt
def fichier_detail(request, fichier_id):
    fichier = get_object_or_404(Fichier, id=fichier_id)
    
    if request.method == 'GET':
        data = {'nom': fichier.nom, 'niveau': fichier.niveau, 'filiere': fichier.filiere, 'groupe': fichier.groupe}
        return JsonResponse(data)
    
    elif request.method == 'PUT':
        data = json.loads(request.body)
        fichier.nom = data['nom']
        fichier.save()
        return JsonResponse({'message': 'Fichier mis à jour avec succès'})
    
    elif request.method == 'DELETE':
        fichier.delete()
        return JsonResponse({'message': 'Fichier supprimé avec succès'})

def inscription(request):
    # Logique pour l'inscription d'un nouvel étudiant
    if request.method == 'POST':
        # Traitement de l'inscription
        return JsonResponse({'message': 'Inscription réussie'})

def authentification(request):
    # Logique d'authentification de l'étudiant
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Authentification réussie'})
        else:
            return JsonResponse({'message': 'Authentification échouée'})

def lire_fichiers(request):
    # Logique pour lire et télécharger tous les fichiers
    fichiers = Fichier.objects.all()
    # Serializer les fichiers si nécessaire
    return JsonResponse({'fichiers': fichiers})

def notifier_admin(instance):
    # Logique pour notifier l'admin lorsqu'un étudiant ajoute un fichier
    # Ici, vous pouvez implémenter la logique d'envoi de notification à l'admin
    pass

@receiver(pre_save, sender=Fichier)
def valider_fichier(sender, instance, **kwargs):
    # Logique pour valider le fichier ajouté par l'étudiant
    if instance.etudiant is not None:
        notifier_admin(instance)
        # Ici, vous pouvez implémenter la logique de validation par l'admin
        # Si l'admin accepte le fichier, il est enregistré dans la base de données
        # Sinon, l'application envoie une notification à l'étudiant
        pass

def ajouter_fichier(request):
    # Logique pour ajouter un nouveau fichier pour sa filière, son niveau et son groupe
    if request.method == 'POST':
        user = request.user
        etudiant = Etudiant.objects.get(user=user)
        nom = request.POST.get('nom')
        description = request.POST.get('description')
        filiere = etudiant.filiere
        niveau = etudiant.niveau
        groupe = etudiant.groupe
        # Créer le nouveau fichier pour sa filière, son niveau et son groupe
        # Logique pour créer un nouveau fichier
        nouveau_fichier = Fichier.objects.create(nom=nom, description=description, filiere=filiere, niveau=niveau, groupe=groupe, etudiant=etudiant)
        return JsonResponse({'message': 'Demande d\'ajout de fichier envoyée à l\'admin'})


from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import  Etudiant
from fichier.models import Fichier

class DelegueView(Etudiant):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def authentification_delegue(self, request):
        # Logique d'authentification du délégué
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'message': 'Authentification en tant que délégué réussie'})
            else:
                return JsonResponse({'message': 'Authentification en tant que délégué échouée'})

    def lister_fichiers(self):
        # Logique pour lister les fichiers appartenant à son niveau, sa filière et son groupe
        fichiers = Fichier.objects.filter(niveau=self.niveau, filiere=self.filiere, groupe=self.groupe)
        # Serializer les fichiers si nécessaire
        return JsonResponse({'fichiers': fichiers})

    def ajouter_fichier(self, request):
        # Logique pour ajouter un nouveau fichier pour son niveau, sa filière et son groupe
        if request.method == 'POST':
            nom = request.POST.get('nom')
            description = request.POST.get('description')
            # Créer le nouveau fichier pour son niveau, sa filière et son groupe
            # Logique pour créer un nouveau fichier
            nouveau_fichier = Fichier.objects.create(nom=nom, description=description, filiere=self.filiere, niveau=self.niveau, groupe=self.groupe, etudiant=self)
            return JsonResponse({'message': 'Nouveau fichier ajouté avec succès'})

    def modifier_fichier(self, request, fichier_id):
        # Logique pour modifier un fichier appartenant à son niveau, sa filière et son groupe
        fichier = Fichier.objects.get(id=fichier_id)
        if fichier.niveau == self.niveau and fichier.filiere == self.filiere and fichier.groupe == self.groupe:
            # Modifier le fichier
            # Logique pour modifier un fichier
            return JsonResponse({'message': 'Fichier modifié avec succès'})
        else:
            return JsonResponse({'message': 'Vous n\'êtes pas autorisé à modifier ce fichier'})

    def supprimer_fichier(self, request, fichier_id):
        # Logique pour supprimer un fichier appartenant à son niveau, sa filière et son groupe
        fichier = Fichier.objects.get(id=fichier_id)
        if fichier.niveau == self.niveau and fichier.filiere == self.filiere and fichier.groupe == self.groupe:
            # Supprimer le fichier
            fichier.delete()
            return JsonResponse({'message': 'Fichier supprimé avec succès'})
        else:
            return JsonResponse({'message': 'Vous n\'êtes pas autorisé à supprimer ce fichier'})
