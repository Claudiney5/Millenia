from django import forms
from django.forms import ModelForm

from . models import *

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = '__all__'
        