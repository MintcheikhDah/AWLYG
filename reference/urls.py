from django.urls import path
from . import views

urlpatterns = [
    #path('fichiers/', views.fichier_list, name='fichier_list'),
    path('groupe/ajouter', views.GroupeViews.ajouter_groupe, name='ajouter_groupe'),
    path('niveau/ajouter', views.NiveauViews.ajouter_niveau, name='ajouter_niveau'),
    path('filiere/ajouter', views.FiliereViews.ajouter_filiere, name='ajouter_filiere'),
    path('annee/ajouter', views.AnneeUniversitaireViews.ajouter_annee, name='ajouter_annee'),
    #path('filiere/ajouter', views.ajouter_filiere, name='ajouter_filiere'),

   path('groupe/ajouter', views.GroupeViews.ajouter_groupe, name='ajouter_groupe'),
    path('niveau/ajouter', views.NiveauViews.ajouter_niveau, name='ajouter_niveau'),
    path('filiere/ajouter', views.FiliereViews.ajouter_filiere, name='ajouter_filiere'),
    path('annee/ajouter', views.AnneeUniversitaireViews.ajouter_annee, name='ajouter_annee'),

    path('groupe/modifier', views.GroupeViews.modifier_groupe, name='modifier_groupe'),
    path('niveau/modifier', views.NiveauViews.modifier_niveau, name='modifier_niveau'),
    path('filiere/modifier', views.FiliereViews.modifier_filiere, name='modifier_filiere'),
    path('annee/modifier', views.AnneeUniversitaireViews.modifier_annee, name='modifier_annee'),

    path('groupes/lister', views.GroupeViews.lister_groupes, name='lister_groupes'),
    path('niveaux/lister', views.NiveauViews.lister_niveaux, name='lister_niveaux'),
    path('filieres/lister', views.FiliereViews.lister_filieres, name='lister_filieres'),
    path('annees/lister', views.AnneeUniversitaireViews.lister_annees, name='lister_annees'),
]