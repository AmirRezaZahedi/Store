from django import forms


class product_detailform(forms.Form):

    CHOICES=(
        (0,"تعدادی"),
        (1,"کیلویی"),
       
      
    )

    name = forms.CharField()
    image = forms.ImageField()
    price = forms.PositiveIntegerField()
    quantity = forms.PositiveIntegerField()
    product_quantity = forms.IntegerField(choices=CHOICES)

class productform(forms.Form):

    CHOICES=(
        (0,"تعدادی"),
        (1,"کیلویی"),
       
      
    )

    name = forms.CharField()
    image = forms.ImageField()
    price = forms.PositiveIntegerField()
    quantity = forms.PositiveIntegerField()
    


     