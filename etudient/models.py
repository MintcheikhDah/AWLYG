from django.db import models
from reference.models import Niveau, Groupe, Filiere, AnneeUniversitaire
from django.contrib.auth.models import AbstractUser,Group,Permission,User
from django.utils import timezone

class Utilisateur(AbstractUser):
    
    email = models.EmailField(unique=True)
    matricule = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(default=timezone.now)
    date_joined = models.DateTimeField(default=timezone.now)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True,
    )

class Etudiant(models.Model):
    id = models.AutoField(primary_key=True, default=1)
    user = models.ForeignKey(Utilisateur, on_delete=models.DO_NOTHING,  related_name='etudiant',null=True)
    niveau = models.ForeignKey(Niveau, on_delete=models.DO_NOTHING)
    filiere = models.ForeignKey(Filiere, on_delete=models.DO_NOTHING)
    annee = models.ForeignKey(AnneeUniversitaire, on_delete=models.DO_NOTHING)
    groupe = models.ForeignKey(Groupe, on_delete=models.DO_NOTHING)
    
class Delegue(models.Model):
    id = models.AutoField(primary_key=True, default=1)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.DO_NOTHING, null=True, default=None, related_name='delegue')
    is_delegue = models.BooleanField(default=False)
   