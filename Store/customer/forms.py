from django import forms


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
    number = forms.IntegerField(min_value=0)
    