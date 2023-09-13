from django.db import models
from Accounts.models import Seller
# Create your models here.
class Product(models.Model):
    CHOICES=(
        (0,"تعدادی"),
        (1,"کیلویی"),
        
    )
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    image = models.ImageField()
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    product_quantity = models.IntegerField(choices=CHOICES)


class staticFeature(models.Model):

    featureName = models.CharField(max_length=20)
    products = models.ManyToManyField(Product)
    childfeatures = models.ManyToManyField('self')
    
    
class dynamicFeature(models.Model):

    featureName = models.CharField(max_length=20)
    products = models.ManyToManyField(Product)
    baseFeature = models.ForeignKey(staticFeature, on_delete=models.CASCADE)


