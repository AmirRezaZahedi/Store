from django.db import models
from Seller.models import Product
from Accounts.models import Customer
# Create your models here.
class Cart(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    number = models.PositiveIntegerField()
