from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Etudiant, Delegue

User = get_user_model()

# l creation d'un etudiant
class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = ['id','username', 'email','password', 'matricule', 'niveau', 'filiere', 'annee', 'groupe', 'est_etudient']

# l creation d'un delegue
class DelegueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delegue
        fields = ['id', 'matricule', 'niveau', 'filiere', 'annee', 'groupe', 'is_delegue']
        extra_kwargs = {'is_delegue': {'default': True}}

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password('1234') 
        user.save()
        return user

# liste l users



#liste l etudiant
class ESerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Etudiant
        fields = '__all__'


#liste l delegue
class DSerializer(serializers.ModelSerializer):
    etudiant = ESerializer()

    class Meta:
        model = Delegue
        fields = '__all__'

#login

#login
class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = ['username', 'password']

class DelegueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delegue
        fields = ['username', 'password']