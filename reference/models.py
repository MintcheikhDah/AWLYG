from django.db import models
class Niveau(models.Model):
    niveau_choices = [("L1", "L1"), ("L2","L2"),("L3","M1"),("M1","M2"),("M3","D1"),("D1","D2"),("D2","D3")]
    id_niveau = models.AutoField(primary_key=True)
    niveau = models.CharField(choices=niveau_choices, max_length=2)

class Filiere(models.Model):
    id_filiere = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)

class Groupe(models.Model):
    id_groupe = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=5, default="A",blank = False)

class AnneeUniversitaire(models.Model):
    annee_debut = models.IntegerField()
    annee_fin = models.IntegerField()

    def __str__(self):
        return f"{self.annee_debut}-{self.annee_fin}"
