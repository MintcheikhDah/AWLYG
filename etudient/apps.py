from django.apps import AppConfig

class EtudientConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'etudient'

class DelegueConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'delegue'

class UtilisateurConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'utilisateur'