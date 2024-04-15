from rest_framework import serializers
from .models import Niveau, Filiere, Groupe, AnneeUniversitaire



class NiveauSerializer(serializers.ModelSerializer):
    class Meta:
        model = Niveau
        fields = ['niveau']

class FiliereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filiere
        fields = '__all__'

class GroupeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groupe
        fields = '__all__'

class AnneeUniversitaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnneeUniversitaire
        fields = '__all__'