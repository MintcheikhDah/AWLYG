from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from os.path import splitext

from reference.models import Niveau, Filiere, Groupe, AnneeUniversitaire,Semester
from typing import List
from django.contrib.auth.models import User

def get_extension(filename):
    return splitext(filename)[1][1:]

class Fichier(models.Model):
    #id_fichier = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100,primary_key=True)
    description = models.TextField()
    date_ajout = models.DateTimeField(auto_now_add=True)
    contenu = models.FileField(upload_to='fichiers/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'odt', 'ods', 'odp', 'zip', 'rar', 'tar', 'gz', 'bz2'])])
    niveau = models.ForeignKey(Niveau, on_delete=models.DO_NOTHING)
    filiere = models.ForeignKey(Filiere, on_delete=models.DO_NOTHING)
    groupe = models.ForeignKey(Groupe, on_delete=models.DO_NOTHING)
    annee_universitaire = models.ForeignKey(AnneeUniversitaire, on_delete=models.DO_NOTHING)
    s =models.ForeignKey(Semester, on_delete=models.DO_NOTHING,default = "S1")
    type = models.CharField(max_length=100, blank=True)
    # user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def types_autorises(self) -> List[str]:
        return [
            'application/pdf',
            'image/jpeg',
            'image/png',
            'application/msword',
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            'application/vnd.ms-excel',
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            'application/vnd.ms-powerpoint',
            'application/vnd.openxmlformats-officedocument.presentationml.presentation',
            'application/vnd.oasis.opendocument.text',
            'application/vnd.oasis.opendocument.spreadsheet',
            'application/vnd.oasis.opendocument.presentation',
            'application/vnd.oasis.opendocument.graphics',
            'application/vnd.oasis.opendocument.chart',
            'application/vnd.oasis.opendocument.formula',
            'application/vnd.oasis.opendocument.database',
            'application/vnd.oasis.opendocument.image',
            'application/vnd.oasis.opendocument.text-master',
            'application/vnd.oasis.opendocument.graphics-template',
            'application/vnd.oasis.opendocument.presentation-template',
            'application/vnd.oasis.opendocument.spreadsheet-template',
            'application/vnd.oasis.opendocument.chart-template',
            'application/vnd.oasis.opendocument.formula-template',
            'application/vnd.oasis.opendocument.drawing',
            'application/vnd.oasis.opendocument.drawing-template',
            'application/vnd.oasis.opendocument.image-template',
            'application/vnd.oasis.opendocument.text-web',
        ]

    def clean(self):
        super().clean()
        extension = get_extension(self.contenu.name)
        if extension not in ['pdf', 'jpg', 'jpeg', 'png', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'odt', 'ods', 'odp', 'zip', 'rar', 'tar', 'gz', 'bz2']:
            raise ValidationError(f"File extension '{extension}' is not allowed. Allowed extensions are: pdf, jpg, jpeg, png, doc, docx, xls, xlsx, ppt, pptx, odt, ods, odp, zip, rar, tar, gz, bz2")

    def save(self, *args, **kwargs):
        self.type = self.detecter_type()
        super(Fichier, self).save(*args, **kwargs)

    def detecter_type(self):
        extension = get_extension(self.contenu.name)
        if extension in ['pdf']:
            return 'Document PDF'
        elif extension in ['jpg', 'jpeg', 'png']:
            return 'Image'
        elif extension in ['doc', 'docx']:
            return 'Document Word'
        elif extension in ['xls', 'xlsx']:
            return 'Document Excel'
        elif extension in ['ppt', 'pptx']:
            return 'Présentation PowerPoint'
        elif extension in ['odt', 'ods', 'odp']:
            return 'Document OpenDocument'
        elif extension in ['zip', 'rar', 'tar', 'gz', 'bz2']:
            return 'Archive compressée'
        else:
            return 'Type inconnu'

