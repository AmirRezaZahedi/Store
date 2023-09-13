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


def dynamic_product_form(intFields, charField, imageField):
    dynamic_fields = {}

    dynamic_fields.update({field: forms.IntegerField() for field in intFields})
    dynamic_fields.update({field: forms.CharField() for field in charField})
    dynamic_fields.update({field: forms.ImageField() for field in imageField})

    dynamic_form_class = type('DynamicProductForm', (product_detailform), dynamic_fields)

    return dynamic_form_class

 

def dynamic_category_form(category):
    dynamic_fields = {}

    CHOICES=((i,category[i])  for i in range(len(category)))
    
    dynamic_fields.update({category: forms.IntegerField(choices=CHOICES) })
    

    dynamic_form_class = type('DynamicCategoryForm', dynamic_fields)

    return dynamic_form_class

     