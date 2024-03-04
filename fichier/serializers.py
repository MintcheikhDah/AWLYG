from rest_framework import serializers
from .models import Fichier

class FichierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fichier
        fields = ['nom', 'description', 'fichier', 'niveau', 'filiere', 'groupe', 'etudiant', 'admin']