﻿from django import forms
from .models import Cart

class filterform(forms.Form):

    CHOICES1=(
        (0,"تعدادی"),
        (1,"کیلویی"),
       
      
    )
    CHOICES2=(
        (0,"تعدادی"),
        (1,"کیلویی"),
       
      
    )
    CHOICES3=(
        (0,"تعدادی"),
        (1,"کیلویی"),
       
      
    )

    
    price = forms.DecimalField(min_value=0)
    quantity = forms.IntegerField(min_value=0)
    collection = forms.ChoiceField(choices=CHOICES1)

class orderform(forms.Form):
    quantity = forms.IntegerField(min_value=0)

class selectform(forms.Form):
    quantity = forms.IntegerField(min_value=0)

class addressform(forms.Form):
    city = forms.CharField(max_length=20)
    address = forms.CharField(widget=forms.Textarea)
    postcode = forms.IntegerField()
