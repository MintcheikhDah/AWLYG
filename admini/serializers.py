from rest_framework import serializers
from .models import Administrateur
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model


class AdministrateurSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Administrateur
        fields = '__all__'

# login




User = get_user_model()


from rest_framework import serializers
from django.contrib.auth import authenticate

class AdministrateurLoginSerializer(serializers.Serializer):
   
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(request=None, username=username, password=password)

        if not user:
            raise serializers.ValidationError("Invalid username or password")

        attrs['user'] = user
        return attrs
# profile
class AdministrateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrateur
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.password = make_password(validated_data.get('password', instance.password))
        instance.save()

        return instance
    

from rest_framework import serializers
from django.contrib.auth import authenticate


