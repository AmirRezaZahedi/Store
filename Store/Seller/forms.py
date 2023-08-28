from django import forms


class product_detailform(forms.Form):

    CHOICES=(
        (0,"تعدادی"),
        (1,"کیلویی"),
       
      
    )

    name = forms.CharField()
    image = forms.ImageField()
    price = forms.DecimalField(min_value=0)
    quantity = forms.IntegerField(min_value=0)
    product_quantity = forms.ChoiceField(choices=CHOICES)

class productform(forms.Form):

    CHOICES=(
        (0,"تعدادی"),
        (1,"کیلویی"),
       
      
    )

    name = forms.CharField()
    image = forms.ImageField()
    price = forms.DecimalField(min_value=0)
    quantity = forms.IntegerField(min_value=0)
    


     