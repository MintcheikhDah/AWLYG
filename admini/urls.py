from django.urls import path
from . import views

urlpatterns = [
    #path('fichiers/', views.fichier_list, name='fichier_list'),
    path("admin/",views.inscription,name="admin"),
    path("admin/",views.inscription,name="admin"),
]