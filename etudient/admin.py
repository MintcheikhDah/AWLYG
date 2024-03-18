from django.contrib import admin
from .models import Etudiant,Delegue,Utilisateur

# Register your models here.
admin.site.register(Etudiant),
admin.site.register(Utilisateur),
admin.site.register(Delegue),
