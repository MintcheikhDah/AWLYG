from django.urls import path
from .views import AdministrateurCreateView,AdministrateurLogoutView,AdministrateurUpdateView,AdministrateurLoginView
urlpatterns = [
    # creer un seul admin
    path('create',AdministrateurCreateView.as_view(), name='administrateur_create'),
    #cree plusieurs admins
     path('admini/', AdministrateurCreateView.as_view(), name='administrateur_create'),
     #deconnexion
    path('logout/', AdministrateurLogoutView.as_view(), name='administrateur_logout'),
    #login
     path('login/', AdministrateurLoginView.as_view(), name='user-login'),
    #modifie le profile
    path('profile/', AdministrateurUpdateView.as_view(), name='administrateur_profile'),
    
]


