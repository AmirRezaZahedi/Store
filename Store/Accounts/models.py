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


