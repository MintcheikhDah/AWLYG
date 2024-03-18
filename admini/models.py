from django.contrib.auth.models import AbstractUser,Permission,Group
from django.db import models
#from rest_framework import permissions
class Administrateur(AbstractUser):
    id = models.AutoField(primary_key=True)
    
    email = models.EmailField(unique=True)
    
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now_add=True,null=True, )
    date_joined = models.DateTimeField(auto_now_add=True,null=True, )

    def is_admin(self):
        return self.is_admin
    groups = models.OneToOneField(
        Group,
        on_delete=models.CASCADE,
        default = None,
        related_name='admin_groups',  # Définissez un related_name unique pour éviter les conflits
    )

    user_permissions = models.OneToOneField(
        Permission,
        on_delete=models.CASCADE,
        default = None,
        related_name='admin_user_permissions',  # Définissez un related_name unique
    )