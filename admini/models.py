from django.db import models
from etudient.models import Etudiant


class Admin(models.Model):
    id_admin = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    numero = models.CharField(max_length=20)
    def __str__(self):
        self.nom

class DemandeAjout(models.Model):
    A_TRAITER = 'AT'
    APPROUVE = 'AP'
    REJETE = 'RE'
    STATUT_CHOICES = [
        (A_TRAITER, 'A traiter'),
        (APPROUVE, 'Approuvé'),
        (REJETE, 'Rejeté'),
    ]
    #from etudient.models import Etudiant

    etudiant = models.ForeignKey(Etudiant, on_delete=models.DO_NOTHING)
    fichier = models.FileField(upload_to='fichiers/')
    statut = models.CharField(max_length=2, choices=STATUT_CHOICES, default=A_TRAITER)
    admin = models.ForeignKey(Admin, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.etudiant.nom
    

