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


class productField(models.Model):

    fieldName = models.CharField(max_length=20)
    
class productValue(models.Model):

    fieldValue = models.CharField(max_length=50)
    
class productDetail(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    productfield = models.ForeignKey(productField, on_delete=models.CASCADE)
    productValue = models.ForeignKey(productValue, on_delete=models.CASCADE)


