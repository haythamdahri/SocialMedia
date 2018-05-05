from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(DemandeAmi)
admin.site.register(DemandeGroupe)
admin.site.register(Conversation)
admin.site.register(Responseconversation)
admin.site.register(Groupe)
admin.site.register(Commentaire)
admin.site.register(Statut)
admin.site.register(Suivie)
admin.site.register(Notification)
admin.site.register(ReseauSocialFile)
admin.site.register(Album)