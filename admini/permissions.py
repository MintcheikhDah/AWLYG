from rest_framework.permissions import BasePermission
from rest_framework.permissions import IsAuthenticated
class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_admin
    
class AdminPermission(IsAuthenticated):
    def has_permission(self, request, view):
        if not request.user.is_authenticated or not request.user.is_admin:
            return False
        return True
    


