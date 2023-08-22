from unittest.util import _MAX_LENGTH
from django.db import models

class users(models.Model):
    user_name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.EmailField()
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    #access=models.BooleanField(max_length=20)
