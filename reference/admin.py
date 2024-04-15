from django.contrib import admin

# Register your models here.from django.contrib import admin
from .models import Filiere,Niveau,AnneeUniversitaire,Groupe,Semester
 

admin.site.register(Filiere),
admin.site.register(Niveau),
admin.site.register(AnneeUniversitaire),
admin.site.register(Groupe),
admin.site.register(Semester),