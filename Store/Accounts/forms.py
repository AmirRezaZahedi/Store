from django import forms
from .models import User

class registerform(forms.Form):

    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()

class seller_registerform(forms.Form):

    CHOICES=(
        (1,"لوازم خانگی"),
        (2,"لبنیات"),
        (3,"شیرینی فروشی"),
        (4,"لوازم الکترونیک"),
        (5,"سوپر مارکت"),
   
      
    )

    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    store_name = forms.CharField()
    store_type = forms.ChoiceField(choices=CHOICES)
     

class loginform(forms.Form):

    username = forms.CharField()
    password = forms.CharField()
    
