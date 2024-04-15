from django.urls import path,include
from .views import EtudiantListView,DelegueListView,EtudiantLoginView,DelegueLoginView
from .views import EtudiantInscriptionView,DelegueCreateView,EtudiantListCreateView,EtudiantRetrieveUpdateDestroyView
urlpatterns = [
    
   
   
    #ajouter
    path('etudiant/inscription/', EtudiantInscriptionView.as_view(), name='etudiant-inscription'),
    path('delegue/create/', DelegueCreateView.as_view(), name='delegate_create'),

    #lister
    #path('users/', UserListView.as_view(), name='user_list'),
    path('etudiants/', EtudiantListView.as_view(), name='etudiant_list'),
    path('delegues/', DelegueListView.as_view(), name='delegue_list'),

    #login
    path('login1/', EtudiantLoginView.as_view(), name='etudiant-login'),
    path('login2/', DelegueLoginView.as_view(), name='delegue-login'),
    path('dj/',include('dj_rest_auth.urls')),

   

    #crud etudiant
    path('etudiant/<int:pk>/', EtudiantRetrieveUpdateDestroyView.as_view(), name='etudiant_retrieve_update_destroy'),
    
    #liste un seul etudiant
    path('etudiant/<int:pk>/', EtudiantListCreateView.as_view(), name='etudiant_list_create'),
   
]
