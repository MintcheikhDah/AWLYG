#from django.conf.urls import url
from etudient import views
from django.urls import path

urlpatterns = [
    path('fichier',views.fichier_detail, name='fichier_detail'),
    #path('list', views.index, name='index'),
    #path('update', views.index, name='index'),
    #path('delete', views.index, name='index'),
    
]




