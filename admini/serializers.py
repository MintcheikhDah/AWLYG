from rest_framework import serializers
from .models import Administrateur

class AdministrateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrateur
        fields = ['id', 'nom', 'email', 'password', 'is_admin']

class AuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class ProfileSerializer(serializers.Serializer):
    nom = serializers.CharField()
    email = serializers.EmailField()
