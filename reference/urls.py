from django.urls import path
from . import views
from .models import Niveau, Filiere, Groupe, AnneeUniversitaire
from .views import NiveauViewSet, FiliereViewSet, GroupeViewSet, AnneeUniversitaireViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'niveaux', NiveauViewSet, basename='niveau')
router.register(r'filieres', FiliereViewSet, basename='filiere')
router.register(r'groupes', GroupeViewSet, basename='groupe')
router.register(r'annees-universitaires', AnneeUniversitaireViewSet, basename='annee-universitaire')

urlpatterns = router.urls

# Pour les méthodes détaillées (get, put, patch, delete)
urlpatterns += [
    path('niveaux/<pk>/', NiveauViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='niveau-detail'),
    path('filieres/<pk>/', FiliereViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='filiere-detail'),
    path('groupes/<pk>/', GroupeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='groupe-detail'),
    path('annees/<pk>/', AnneeUniversitaireViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='annee-universitaire-detail'),
]