from django import forms
from .models import User

class registerform(forms.Form):

    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()

class loginform(forms.Form):

    username = forms.CharField()
    password = forms.CharField()
    
