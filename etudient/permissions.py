from rest_framework.permissions import IsAuthenticated, BasePermission
from .models import Delegue,Etudiant
from admini.models import Administrateur
from rest_framework import permissions

class ModifyProfilePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Logique pour vérifier si l'utilisateur peut modifier son propre profil
        return False  # Retourne True si l'utilisateur peut modifier son profil, False sinon





    
class CreerDeleguePermission(BasePermission):
    def has_permission(self, request, view):
        # Vérifier si l'utilisateur est un administrateur
        if request.user.is_authenticated and hasattr(request.user, 'is_admin'):
            return request.user.is_admin
        return False

class IsDelegueOrAdmin(permissions.BasePermission):
    message = 'Vous n\'êtes pas autorisé à effectuer cette action.'

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_admin:
            return True
        if hasattr(obj, 'etudiant') and hasattr(obj.etudiant, 'user') and request.user == obj.etudiant.user:
            return True
        return False
class IsEtudiantOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.is_admin or hasattr(request.user, 'etudiant'))
