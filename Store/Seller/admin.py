from django.contrib import admin
from .models import Product, staticFeature,dynamicFeature
# Register your models here.

admin.site.register(Product)
admin.site.register(staticFeature)
admin.site.register(dynamicFeature)