from django.urls import path
from .views import  FichierDelete,FichierDownload,FichierUpdate,FichierListCreate

#from django.urls import path

urlpatterns = [
    #path('fichiers/', views.fichier_list, name='fichier_list'),
    #path('', Fichierl.as_view(), name='lister_fichiers'),
    path('ajouter',FichierListCreate.as_view(), name='lister_fichiers'),
    path('modifier/<int:pk>/', FichierUpdate.as_view(), name='fichier_modifier'),
    path('supprimer/<int:pk>/', FichierDelete.as_view(), name='fichier_supprimer'),

    #path('supprimer', FichierDelete.as_view(), name='lister_fichiers'),
    path('telecharger/<int:pk>/',FichierDownload.as_view(), name='lister_fichiers'),
     

]
