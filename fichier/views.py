
#from django.shortcuts import render

from .models import Fichier
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import request
from etudient.models import  Delegue
#from .filter import FichierFilter
from django.shortcuts import render
def fichier_view(request):
    fichiers = Fichier.objects.all()
    return render(request,  {'fichiers': fichiers})


# @api_view(['GET'])
# def get_fichier(request):

#    fichier_filter = FichierFilter(request.GET,queryset=Fichier.objects.all().order_by('id_fichier'))
 #   serializer = FichierFilter(fichier_filter.qs,many=True)
  #  return Response({"fichiers":serializer.data})




def ajouter_fichier(self, request):
    
    if request.method == 'POST':
        nom = request.POST.get('nom')
        description = request.POST.get('description')
        fichier = request.FILES['fichier']
        niveau = request.POST.get('niveau')
        filiere = request.POST.get('filiere')
        groupe = request.POST.get('groupe')

        
        nouveau_fichier = Fichier.objects.create(nom=nom, description=description, fichier=fichier, niveau=niveau, filiere=filiere, groupe=groupe)
        nouveau_fichier.save()
        return Response({'message': ' fichier ajouté avec succès'})



class GestionFichiers:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def lister_fichiers(self, request):
        
        fichiers = Fichier.objects.all()
        
        return Response({'fichiers': fichiers})

    def ajouter_fichier(self, request):
        
        if request.method == 'POST':
            nom = request.POST.get('nom')
            description = request.POST.get('description')
            fichier = request.FILES['fichier']
            niveau = request.POST.get('niveau')
            filiere = request.POST.get('filiere')
            groupe = request.POST.get('groupe')

            
            nouveau_fichier = Fichier.objects.create(nom=nom, description=description, fichier=fichier, niveau=niveau, filiere=filiere, groupe=groupe)
            nouveau_fichier.save()
            return Response({'message': ' fichier ajouté avec succès'})

    def modifier_fichier(self, request, fichier_id):
        # Logique pour modifier un fichier
        if request.method == 'POST':
            fichier = Fichier.objects.get(id=fichier_id)
            nom = request.POST.get('nom')
            description = request.POST.get('description')
            fichier = request.FILES['fichier']
            niveau = request.POST.get('niveau')
            filiere = request.POST.get('filiere')
            groupe = request.POST.get('groupe')

            
            delegue = Delegue.objects.get(user=request.user)
            if delegue.niveau == fichier.niveau and delegue.filiere == fichier.filiere and delegue.groupe == fichier.groupe:

                fichier.nom = nom
                fichier.description = description
                fichier.fichier = fichier
                fichier.niveau = niveau
                fichier.filiere = filiere
                fichier.groupe = groupe
                fichier.save()
                return Response({'message': 'Fichier modifié avec succès'})
            else:
                return Response({'message': 'Vous n\'êtes pas autorisé à modifier ce fichier'})

    def supprimer_fichier(self, request, fichier_id):
        # Logique pour supprimer un fichier
        fichier = Fichier.objects.get(id=fichier_id)
        # Vérifier les autorisations du délégué ou de l'admin pour supprimer le fichier
        # Logique pour vérifier les autorisations
        fichier.delete()
        return Response({'message': 'Fichier supprimé avec succès'})
