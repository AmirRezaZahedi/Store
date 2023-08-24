from django import forms
from .models import User

'''
class registerform(forms.ModelForm):
    class Meta:
        model=User
        fields= ('Username','password','email','first_name','last_name','access')

class loginform(forms.ModelForm):
    class Meta:
        model=User
        fields= ('Username','password','email','first_name','last_name','access')
'''
class registerform(forms.Form):
    Username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
class loginform(forms.Form):
    Username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
