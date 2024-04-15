from django.contrib.auth.models import AbstractUser,Permission,Group
from django.db import models

class Administrateur(AbstractUser):
    
    is_admin = models.BooleanField(default=True)
    

    groups = models.OneToOneField(
        Group,
        on_delete=models.CASCADE,
        default=None,
        related_name='admin_groups',
        null=True,
        blank=True,  
    )

    user_permissions = models.OneToOneField(
        Permission,
        on_delete=models.CASCADE,
        default=None,
        related_name='admin_user_permissions',
        null=True,
        blank=True,  
    )