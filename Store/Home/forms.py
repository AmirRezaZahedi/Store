from django import forms

class detailProduct(forms.Form):
    name = forms.CharField()
    image = forms.ImageField()