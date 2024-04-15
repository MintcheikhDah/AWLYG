from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from.serializers import FichierSerializer 
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics
from django.http import HttpResponse
import os
from django.core.files.storage import default_storage
from django.core.exceptions import ObjectDoesNotExist
from .models import Fichier
import mimetypes


from django.shortcuts import render
from .models import Fichier
from reference.models import Niveau

#ajouter
class FichierListCreate(ListCreateAPIView):
    queryset = Fichier.objects.all()
    serializer_class = FichierSerializer
#supprimer
class FichierDelete(RetrieveUpdateDestroyAPIView):
    queryset = Fichier.objects.all()
    serializer_class = FichierSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
#modifier
class FichierUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Fichier.objects.all()
    serializer_class = FichierSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        instance = serializer.instance
        instance.titre = serializer.validated_data.get('nom', instance.nom)
#telecharger
class FichierDownload(APIView):
    def get_file(self, pk):
        try:
            fichier = Fichier.objects.get(pk=pk)
            file_path = fichier.contenu.path
            content_type, encoding = mimetypes.guess_type(fichier.contenu.name)
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type=content_type)
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(fichier.contenu.name)
                return response
        except ObjectDoesNotExist:
            return Response({"error": "Fichier introuvable"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        return self.get_file(pk)