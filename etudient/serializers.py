from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Etudiant, Delegue

User = get_user_model()

from rest_framework import serializers
from .models import Etudiant,Utilisateur,Delegue

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ('id', 'nom', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

class EtudiantSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Etudiant
        fields = ['id', 'user', 'matricule', 'niveau', 'filiere', 'annee', 'groupe']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        etudiant = Etudiant.objects.create(user=user, **validated_data)
        return etudiant
class DelegueSerializer(serializers.ModelSerializer):
    etudiant = EtudiantSerializer()

    class Meta:
        model = Delegue
        fields = ['id', 'etudiant', 'is_delegue', 'groups', 'user_permissions']

    def create(self, validated_data):
        etudiant_data = validated_data.pop('etudiant')
        etudiant_serializer = EtudiantSerializer(data=etudiant_data)
        if etudiant_serializer.is_valid():
            etudiant = etudiant_serializer.create(etudiant_data)
            delegue = Delegue.objects.create(etudiant=etudiant, **validated_data)
            return delegue
        else:
            raise serializers.ValidationError(etudiant_serializer.errors)
        



class USerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = '__all__'

class ESerializer(serializers.ModelSerializer):
    user = USerializer()
    niveau = serializers.StringRelatedField()
    filiere = serializers.StringRelatedField()
    annee = serializers.StringRelatedField()
    groupe = serializers.StringRelatedField()

    class Meta:
        model = Etudiant
        fields = '__all__'

class DSerializer(serializers.ModelSerializer):
    etudiant = ESerializer()

    class Meta:
        model = Delegue
        fields = '__all__'