from rest_framework import serializers
from .models import Fichier



class FichierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fichier
        fields = [ 'nom', 'description', 'date_ajout', 'contenu', 'niveau', 'filiere', 'groupe', 'annee_universitaire']

