from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ACCESS_CHOICES = [
    (0, 'seller'),
    (1, 'customer'), 
    ]
    

    access = models.IntegerField(
         choices=ACCESS_CHOICES, default=1)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  primary_key=True)
    
class Seller(models.Model):
    CHOICES=(
        (1,"لوازم خانگی"),
        (2,"لبنیات"),
        (3,"شیرینی فروشی"),
        (4,"لوازم الکترونیک"),
        (5,"سوپر مارکت"),
   
      
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE,  primary_key=True)
    store_name = models.CharField(max_length=20)
    store_type = models.IntegerField(choices=CHOICES)