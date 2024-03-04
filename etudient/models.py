from django.db import models
from reference.models import Niveau, Groupe, Filiere, AnneeUniversitaire

class Etudiant(models.Model):
    id_etudiant = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    numero_tel = models.CharField(max_length=20)
    matricule = models.CharField(max_length=20)
    niveau = models.ForeignKey(Niveau, on_delete=models.DO_NOTHING)
    filiere = models.ForeignKey(Filiere, on_delete=models.DO_NOTHING)
    groupe = models.ForeignKey(Groupe, on_delete=models.DO_NOTHING)
    annee = models.ForeignKey(AnneeUniversitaire, on_delete=models.DO_NOTHING )
class Delegue(Etudiant):
    pass