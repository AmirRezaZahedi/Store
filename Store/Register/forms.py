from django import forms
from .models import users

class registerform(forms.ModelForm):
    class Meta:
        modele=users
        feildes="_all_"