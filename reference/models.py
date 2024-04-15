from django.db import models
#from .models import AnneeUniversitaire,Niveau,Semester,Groupe,Filiere
class Niveau(models.Model):
    niveau_choices = [("L1", "L1"), ("L2","L2"),("L3","L3"),("M1","M1"),("M2","M2"),("M3","M3"),("D1","D1"),("D2","D2"),("D3","D3")]
    niveau = models.CharField(choices=niveau_choices, max_length=2,unique=True,primary_key=True)
    annee = models.ForeignKey("AnneeUniversitaire",  on_delete=models.CASCADE)

class Filiere(models.Model):
    nom = models.CharField(max_length=100,primary_key=True)
    niveau=models.ForeignKey("Niveau", on_delete=models.CASCADE)

class Groupe(models.Model):
    nom = models.CharField(max_length=5, default="A",blank = False,primary_key=True)
    filiere = models.ForeignKey("Filiere",  on_delete=models.CASCADE)
    niveau = models.ForeignKey("Niveau",  on_delete=models.CASCADE)

class Semester(models.Model):
    s = [("S1","S1"),("S2","S2"),("S3","S3"),("S4","S4"),("S5","S5"),("S6","S6")]
    nom = models.CharField(choices=s, max_length=2,unique=True,primary_key=True)
    niveau = models.ForeignKey("Niveau",  on_delete=models.CASCADE)
    filiere = models.ForeignKey("Filiere",   on_delete=models.CASCADE)


class AnneeUniversitaire(models.Model):
    annee_debut = models.IntegerField()
    annee_fin = models.IntegerField()
    a = models.CharField(primary_key=True, default='' ,max_length=9)

    def save(self, *args, **kwargs):
        self.a = f"{self.annee_debut}_{self.annee_fin}"
        super(AnneeUniversitaire, self).save(*args, **kwargs)

    def __str__(self):
        return self.a
