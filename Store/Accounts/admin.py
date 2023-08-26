from django.contrib import admin
from .models import User
from .models import Seller, Customer


admin.site.register(User)
admin.site.register(Seller)
admin.site.register(Customer)