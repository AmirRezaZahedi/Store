from django.db import models
from Seller.models import Product
from Accounts.models import Seller
# Create your models here.
class Cart(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    number = models.PositiveIntegerField()
