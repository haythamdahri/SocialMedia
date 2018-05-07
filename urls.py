from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include,url
from django.conf.urls.static import settings, static
from . import views
from django.contrib.auth import views as auth_views

app_name = "SocialMedia"

urlpatterns = [
    path('profil/', views.profil, name='profil'),
    path('ajaxuser/', views.ajaxUser, name="AjaxUser"),
    path('login', views.log_in, name='login'),
    path('logout', views.log_out, name='logout'),
    path('signup', views.register, name='signup'),
    path('profil/demandes', views.demandesProfil, name="demandes"),
    path('profil/media', views.mediaProfil, name="mediaProfil"),
    path('supprimer-ami/', views.suprimerAmi, name="supprimerAmi"),
    url('rechercher-amis', views.rechercherAmis, name="rechercherAmis"),
    path('chat', views.chat, name="chat"),
    path('uploads', views.uploads.as_view(), name="uploads"),

    path('reset-password/', views.password_reset, name='password_reset'),

    path('reset-password/done/', auth_views.password_reset_done,
        {'template_name': 'registration/reset_password_done.html'},name='password_reset_done'),

    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm,
        {'template_name': 'registration/reset_password_confirm.html',
         'post_reset_redirect': 'SocialMedia:password_reset_complete'}, name='password_reset_confirm'),

    path('reset-password/complete/', auth_views.password_reset_complete,
        {'template_name': 'registration/reset_password_complete.html'}, name='password_reset_complete'),

    path('changephotocouverture', views.changephotocouverture, name="changephotocouverture"),

    path('changephotoprofil', views.changephotoprofil, name="changephotoprofil"),

    path('profil/groupes', views.groupesProfil, name="groupes"),

    path('demandeajax', views.demandeViaAjax, name="demandeViaAjax"),

    path('profil/editInterface/', views.editInterface, name="editInterface"),

    path('profil/edit-about/', views.editAbout, name="editAbout"),

    path('profil/edit-experience/<int:pk>/', views.editExperience, name="editExperience"),

    path('profil/edit-formation/<int:pk>/', views.editFormation, name="editFormation"),

    path('', views.home, name="home"),

]