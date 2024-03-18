from rest_framework import permissions

class AdministrateurPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj=None):
        return request.user.is_superuser

    def has_permission(self, request, view):
        return request.user.is_superuser