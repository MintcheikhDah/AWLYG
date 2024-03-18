from rest_framework import serializers
from .models import Fichier



class FichierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fichier
        fields = ['id_fichier', 'nom', 'description', 'date_ajout', 'contenu', 'niveau', 'filiere', 'groupe', 'anne_universitaire']

