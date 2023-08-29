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
         (0,"لوازم خانگی"),
         (1,"لبنیات"),
         (2,"شیرینی فروشی"),
         (3,"لوازم الکترونیک"),
         (4,"سوپر مارکت"),
    
      
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE,  primary_key=True, related_name='seller')
    store_name = models.CharField(max_length=20)
    store_type = models.IntegerField(choices=CHOICES)