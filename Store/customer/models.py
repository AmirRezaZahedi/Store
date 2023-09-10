from django.db import models
from Seller.models import Product
from Accounts.models import Customer,Seller


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='+')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField()

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='+')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField()
