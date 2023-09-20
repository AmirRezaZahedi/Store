from django.contrib import admin
from .models import Product, staticFeature,charDynamicFeature,ImageDynamicFeature,intDynamicFeature
# Register your models here.

admin.site.register(charDynamicFeature)
admin.site.register(ImageDynamicFeature)
admin.site.register(intDynamicFeature)
admin.site.register(Product)