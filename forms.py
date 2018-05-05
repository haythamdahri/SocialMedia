from django import forms
from main_app.models import *
from django import forms
from django.core.exceptions import ValidationError

from .models import *
from django.contrib.auth.admin import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import datetime

class loginform(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
   ### class Meta:
      ###  model = User
       ### fields = ['username', 'password']


class PhotoForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = Image
        fields = '__all__'

class demandeForm(forms.Form):
    demande = forms.IntegerField(widget=forms.HiddenInput)
    statut = forms.IntegerField(widget=forms.HiddenInput)