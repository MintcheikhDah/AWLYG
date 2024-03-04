from rest_framework import serializers
from .models import Niveau,Filiere,Groupe

class NiveauSerializer(serializers.ModelSerializer):
    class Meta:
        model = Niveau
        fields = ['nom']