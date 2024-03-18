from django.urls import path
from .views import CreerUtilisateurView, CreerEtudiantView, CreerDelegueView,UserListView,EtudiantListView,DelegueListView

urlpatterns = [
    path('creer-utilisateur/', CreerUtilisateurView.as_view(), name='creer_utilisateur'),
    path('creer-etudiant/', CreerEtudiantView.as_view(), name='creer_etudiant'),
    path('creer-delegue/', CreerDelegueView.as_view(), name='creer_delegue'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('etudiants/', EtudiantListView.as_view(), name='etudiant_list'),
    path('delegues/', DelegueListView.as_view(), name='delegue_list'),
]