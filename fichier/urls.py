from django.urls import path
from .views import  FichierDelete,FichierDownload,FichierUpdate,FichierListCreate

#from django.urls import path

urlpatterns = [
    
    path('ajouter',FichierListCreate.as_view(), name='lister_fichiers'),
    path('modifier/<pk>/', FichierUpdate.as_view(), name='fichier_modifier'),
    path('supprimer/<pk>/', FichierDelete.as_view(), name='fichier_supprimer'),

    
    path('telecharger/<pk>/',FichierDownload.as_view(), name='lister_fichiers'),
     

]
