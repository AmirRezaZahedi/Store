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
    fieldValue = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)