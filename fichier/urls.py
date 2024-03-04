from django.urls import path
from . import views 

#from django.urls import path

urlpatterns = [
    #path('fichiers/', views.fichier_list, name='fichier_list'),
    path('fichiers/ajouter', view=views.ajouter_fichier, name='lister_fichiers'),
]
