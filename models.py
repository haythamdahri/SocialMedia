import os.path
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from main_app.models import Profil, Image

from main_app.models import *
# Create your models here.


class Notification(models.Model):
    url = models.URLField(max_length=500)
    message = models.CharField(max_length=1000)
    is_read = models.BooleanField(default=False)
    read_date = models.DateTimeField(default=False)
    profil_to_notify = models.ForeignKey(Profil, on_delete=models.CASCADE)


class Groupe(models.Model):
    statuts = (('publique', 'publique'), ('prive', 'privé'))
    nom = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    date_creation = models.DateField()
    statut_groupe = models.CharField(choices=statuts, max_length=255, null=False, blank=False)
    photo_profil = models.OneToOneField(Image, on_delete=models.CASCADE, related_name="groupe_photo")
    photo_couverture = models.OneToOneField(Image, on_delete=models.CASCADE, related_name="profil_cover")
    admins = models.ManyToManyField(Profil, related_name="admin")
    mederators = models.ManyToManyField(Profil, related_name="moderateur")
    creator = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="createur")
    adherents = models.ManyToManyField(Profil, related_name="adherent")

    def __str__(self):
        return "Groupe: "+self.nom+"\b\bCree Par: "+self.creator.user.username


class DemandeGroupe(models.Model):
    emetteur = models.ForeignKey(Profil, on_delete=models.CASCADE)
    groupe_recepteur = models.OneToOneField(Groupe, on_delete=models.CASCADE)
    reponse  = models.BooleanField()

    def __str__(self):
        return self.emetteur.user.username+" à demandé de rejoidre le groupe "+self.groupe_recepteur.nom

class Like(models.Model):
    user = models.ForeignKey(Profil, on_delete=models.CASCADE)
    like_date_time = models.DateTimeField(auto_now_add=now())


class Statut(models.Model):
    date_statut = models.DateTimeField()
    contenu_statut = models.CharField(max_length=6000)
    is_group_statut = models.BooleanField(default=False)
    is_profil_statut = models.BooleanField(default=False)
    publisher = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="publisher")
    mur_profil = models.ForeignKey(Profil, on_delete=models.CASCADE, null=True, blank=True, related_name="mur_profil")
    mur_groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE, null=True, blank=True)
    likes = models.ManyToManyField(Like)


class Commentaire(models.Model):
    comment = models.CharField(null=False, blank=False, max_length=6000)
    date_commentaire = models.DateField()
    statut = models.OneToOneField(Statut, on_delete=models.CASCADE)
    user = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="commented_user")
    have_image = models.BooleanField(default=False)
    image = models.OneToOneField(Image, on_delete=models.CASCADE)
    likes = models.ManyToManyField(Like)


class DemandeAmi(models.Model):
    demandes = ((0,'En Cours'),(1,'Acceptée'),(2,'Refusée'),(3,'Bloquée'))
    emetteur = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="sender")
    recepteur = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="receiver")
    statut = models.IntegerField(null=False, blank=False, choices=demandes)

    class Meta:
        unique_together = (['emetteur', 'recepteur'])
        ordering = ['id']

    def __str__(self):
        return self.demandes[self.statut][1]

class Suivie(models.Model):
    follower = models.ForeignKey(Profil, on_delete = models.CASCADE, related_name="suiveur")
    followed_profil = models.ForeignKey(Profil, on_delete= models.CASCADE, related_name="suive")



class Conversation(models.Model):
    start_date = models.DateTimeField(blank=False)
    participants = models.ManyToManyField(User)

    def __str__(self):
        show = ""
        for user in self.participants.all():
            show += " || Participant Username: " + user.username
        return show


class Responseconversation(models.Model):
    message = models.CharField(max_length=6000)
    message_date = models.DateTimeField(blank=False)
    is_image = models.BooleanField(default=False)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True, null=True)
    user_responsed = models.ForeignKey(User, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return "Response Of: "+self.user_responsed.username


VALID_IMAGE_EXTENSIONS = [
    "jpg",
    "jpeg",
    "png",
    "gif",
]


def generate_path(instance, filename):
    extension = os.path.splitext(filename)[1][1:]
    print(extension)
    if extension in VALID_IMAGE_EXTENSIONS:
        path = 'SocialMedia/Image/'
    else:
        path = 'SocialMedia/Fichier/'

    return os.path.join(path, instance.fichier.name)

class Album(models.Model):
    nom = models.CharField(max_length=300)
    date_creation = models.DateField()
    user = models.ForeignKey(Profil, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class ReseauSocialFile(models.Model):
    fichier = models.FileField(upload_to=generate_path)
    date_telechargement = models.DateTimeField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True,blank=True)
    user = models.ForeignKey(Profil, on_delete=models.CASCADE)
    likes = models.ManyToManyField(Like)
    comment = models.ManyToManyField(Commentaire)

    def __str__(self):
        return self.fichier.name


class Poste(models.Model):
    nom_poste = models.CharField(max_length=300)

    def __str__(self):
        return self.nom_poste


class OffreEmploi(models.Model):
    TYPES_EMPLOI = (('plein', 'Plein temps'), ('partiel', 'Temps partiel'))
    tel = models.IntegerField()
    email = models.EmailField()
    pays = models.CharField(max_length=300)
    ville = models.CharField(max_length=300)
    diplome_requis = models.CharField(max_length=300)
    type_contrat = models.CharField(max_length=300)
    description_poste = models.TextField()
    profil_recherche = models.TextField()
    presentation_entreprise = models.TextField()
    poste = models.ForeignKey(Poste, on_delete=models.CASCADE,null=True, blank=True,related_name="poste_recherche", default="")
    type_emploi = models.CharField(max_length=300, choices=TYPES_EMPLOI, null=True, blank=True, default="")
    nom_poste = models.CharField(max_length=300, null=True, blank=True)
    en_cours = models.BooleanField()
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    profil_publicateur = models.ForeignKey(Profil, on_delete=models.CASCADE,related_name="profil_publicateur")
    profil_postulants = models.ManyToManyField(Profil, related_name="profil_postulants")

    def __str__(self):
        return self.nom_poste

class Experience(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE,null=True, blank=True)
    nom_entreprise = models.CharField(max_length=300)
    poste = models.ForeignKey(Poste, on_delete=models.CASCADE,null=True, blank=True)
    nom_poste = models.CharField(max_length=300)
    date_debut = models.DateField()
    date_fin = models.DateField( null=True, blank=True)
    actuel = models.BooleanField()
    description = models.TextField( null=True, blank=True)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)


class Ecole(models.Model):
    nom = models.CharField(max_length=300)
    logo = models.ImageField(upload_to="SocialMedia/Image/")

    def __str__(self):
        return self.nom


class Formation(models.Model):
    titre_formation = models.CharField( max_length=300, null=True, blank=True)
    ecole = models.ForeignKey(Ecole, on_delete=models.CASCADE,null=True, blank=True)
    nom_ecole = models.CharField(max_length=300, null=True,blank=True, default="")
    nom_formation = models.CharField(max_length=300, null=True)
    domaine = models.CharField(max_length=300, null=True, blank=True)
    resultat_obtenu = models.CharField(max_length=300, null=True, blank=True)
    activite_et_associations = models.TextField( null=True, blank=True)
    annee_debut = models.DateField()
    annee_fin = models.DateField()
    description = models.TextField( null=True, blank=True)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)


class Organisme(models.Model):
    nom = models.CharField(max_length=300)
    logo = models.ImageField(upload_to="SocialMedia/Image/")


class ActionBenevole(models.Model):
    organisme = models.ForeignKey(Organisme, on_delete=models.CASCADE,null=True, blank=True)
    nom_organisme = models.CharField(max_length=300)
    poste = models.ForeignKey(Poste, on_delete=models.CASCADE,null=True, blank=True)
    nom_poste = models.CharField(max_length=300)
    cause = models.TextField(null=True, blank=True)
    date_debut = models.DateField()
    date_fin = models.DateField()
    description = models.TextField(null=True, blank=True)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, default="", null=True, blank=True)


class Langue(models.Model):
    NIVEAU_LANGUE = (('debutant', 'Débutant'), ('intermediaire', 'Intermédiaire'), ('expert', 'Expert'))
    nom = models.CharField(max_length=300)
    niveau = models.CharField(max_length=300, choices=NIVEAU_LANGUE)
    profils = models.ManyToManyField(Profil, related_name="profils")
    
