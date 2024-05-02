from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
class BoxeurForm(ModelForm):
    class Meta:
        model = models.Boxeur
        fields = ('titre', 'boxeur', 'date_parution', 'nombre_pages','resume')
        labels = {
        'titre' : _('Titre'),
        'boxeur' : _('Auteur') ,
        'date_parution' : _('Date de parution'),
        'nombre_pages' : _('Nombre de pages'),
        'resume' : _('Résumé')
        }
