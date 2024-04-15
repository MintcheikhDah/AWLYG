from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from reference.models import Niveau, AnneeUniversitaire, Groupe, Filiere

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        #extra_fields = {'est_delegue': True, 'est_prof': True}
        user = self.create_user(username, email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

class Etudiant(CustomUser):
    est_etudiant = models.BooleanField(default=True)
    matricule = models.CharField(max_length=100, null=True, blank=True)
    niveau = models.ForeignKey(Niveau, on_delete=models.DO_NOTHING, blank=True, null=True)
    filiere = models.ForeignKey(Filiere, on_delete=models.DO_NOTHING, blank=True, null=True)
    annee = models.ForeignKey(AnneeUniversitaire, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.username

class Delegue(CustomUser):
    est_delegue = models.BooleanField(default=True)
    #est_prof = models.BooleanField(default=False)
    #departement = models.ForeignKey(Departement, on_delete=models.DO_NOTHING, blank=True, null=True)
    est_actif = models.BooleanField(default=True)
    matricule = models.CharField(max_length=100, null=True, blank=True)
    niveau = models.ForeignKey(Niveau, on_delete=models.DO_NOTHING, blank=True, null=True)
    filiere = models.ForeignKey(Filiere, on_delete=models.DO_NOTHING, blank=True, null=True)
    annee = models.ForeignKey(AnneeUniversitaire, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.username