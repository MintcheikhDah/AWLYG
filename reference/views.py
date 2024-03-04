#from django.http import JsonResponse
from .models import Niveau, Filiere, Groupe, AnneeUniversitaire
from rest_framework.decorators import api_view
from rest_framework.response import Response
class NiveauViews:
    def lister_niveaux(self, request):
        niveaux = Niveau.objects.all()
        # Serializer les niveaux si nécessaire
        return Response({'niveaux': niveaux})

    def ajouter_niveau(self, request):
        if request.method == 'POST':
            nom = request.POST.get('nom')
            niveau = Niveau.objects.create(nom=nom)
            return Response({'message': 'Niveau ajouté avec succès'})

    def modifier_niveau(self, request, niveau_id):
        if request.method == 'POST':
            niveau = Niveau.objects.get(id=niveau_id)
            nom = request.POST.get('nom')
            niveau.nom = nom
            niveau.save()
            return Response({'message': 'Niveau modifié avec succès'})

    def supprimer_niveau(self, request, niveau_id):
        niveau = Niveau.objects.get(id=niveau_id)
        niveau.delete()
        return Response({'message': 'Niveau supprimé avec succès'})

class FiliereViews:
    def lister_filieres(self, request):
        filieres = Filiere.objects.all()
        # Serializer les filières si nécessaire
        return Response({'filieres': filieres})

    def ajouter_filiere(self, request):
        if request.method == 'POST':
            nom = request.POST.get('nom')
            filiere = Filiere.objects.create(nom=nom)
            return Response({'message': 'Filière ajoutée avec succès'})

    def modifier_filiere(self, request, filiere_id):
        if request.method == 'POST':
            filiere = Filiere.objects.get(id=filiere_id)
            nom = request.POST.get('nom')
            filiere.nom = nom
            filiere.save()
            return Response({'message': 'Filière modifiée avec succès'})

    def supprimer_filiere(self, request, filiere_id):
        filiere = Filiere.objects.get(id=filiere_id)
        filiere.delete()
        return Response({'message': 'Filière supprimée avec succès'})

class GroupeViews:
    def lister_groupes(self, request):
        groupes = Groupe.objects.all()
        # Serializer les groupes si nécessaire
        return Response({'groupes': groupes})

    def ajouter_groupe(self, request):
        if request.method == 'POST':
            nom = request.POST.get('nom')
            groupe = Groupe.objects.create(nom=nom)
            return Response({'message': 'Groupe ajouté avec succès'})

    def modifier_groupe(self, request, groupe_id):
        if request.method == 'POST':
            groupe = Groupe.objects.get(id=groupe_id)
            nom = request.POST.get('nom')
            groupe.nom = nom
            groupe.save()
            return Response({'message': 'Groupe modifié avec succès'})

    def supprimer_groupe(self, request, groupe_id):
        groupe = Groupe.objects.get(id=groupe_id)
        groupe.delete()
        return Response({'message': 'Groupe supprimé avec succès'})

class AnneeUniversitaireViews:
    def lister_annees(self, request):
        annees = AnneeUniversitaire.objects.all()
        # Serializer les années universitaires si nécessaire
        return Response({'annees': annees})

    def ajouter_annee(self, request):
        if request.method == 'POST':
            annee_debut = request.POST.get('annee_debut')
            annee_fin = request.POST.get('annee_fin')
            annee = AnneeUniversitaire.objects.create(annee_debut=annee_debut, annee_fin=annee_fin)
            return Response({'message': 'Année universitaire ajoutée avec succès'})

    def modifier_annee(self, request, annee_id):
        if request.method == 'POST':
            annee = AnneeUniversitaire.objects.get(id=annee_id)
            annee_debut = request.POST.get('annee_debut')
            annee_fin = request.POST.get('annee_fin')
            annee.annee_debut = annee_debut
            annee.annee_fin = annee_fin
            annee.save()
            return Response({'message': 'Année universitaire modifiée avec succès'})

    def supprimer_annee(self, request, annee_id):
        annee = AnneeUniversitaire.objects.get(id=annee_id)
        annee.delete()
        return Response({'message': 'Année universitaire supprimée avec succès'})
