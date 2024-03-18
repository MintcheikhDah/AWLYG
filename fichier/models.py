from django.db import models

# Create your models here.

from reference.models import Niveau,Filiere,Groupe, AnneeUniversitaire
from typing import List
from django.contrib.auth.models import User
class Fichier(models.Model):
    id_fichier = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    description = models.TextField()
    date_ajout = models.DateTimeField(auto_now_add=True)
    contenu = models.FileField(upload_to='fichiers/')
    niveau = models.ForeignKey(Niveau, on_delete=models.DO_NOTHING)
    filiere = models.ForeignKey(Filiere, on_delete=models.DO_NOTHING)
    groupe = models.ForeignKey(Groupe, on_delete=models.DO_NOTHING)
    anne_universitaire = models.ForeignKey(AnneeUniversitaire, on_delete=models.DO_NOTHING)
    #user = models.ForeignKey(User , on_delete=models.DO_NOTHING)
    def types_autorises(self) -> List[str]:
        return ['application/pdf', 'image/jpeg', 'image/png']
