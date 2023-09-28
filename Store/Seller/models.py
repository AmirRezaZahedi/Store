from django.db import models
from Accounts.models import Seller

class Category(models.Model):

    categoryName = models.CharField(max_length=20)
    referenceCategory = models.ForeignKey('self',on_delete=models.CASCADE)


    def findRoot(self):
        features = []
        categoryRoot = self
        while(categoryRoot.referenceCategory != null):
            features.append(categoryRoot.staticfeature_set.all())
            categoryRoot = categoryRoot.referenceCategory
        return features




class Product(models.Model):
    CHOICES=(
        (0,"تعدادی"),
        (1,"کیلویی"),
        
    )
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    product_quantity = models.IntegerField(choices=CHOICES)
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class staticFeature(models.Model):

    featureName = models.CharField(max_length=20)
    feature = models.ManyToManyField('self')

    category = models.ManyToManyField(Category)

    @staticmethod
    def findFeature(features, fields):

        return
    
    
class intDynamicFeature(models.Model):

    featureNumber = models.IntegerField()
    products = models.ManyToManyField(Product)
    baseFeature = models.ForeignKey(staticFeature, on_delete=models.CASCADE)


class charDynamicFeature(models.Model):

    featureName = models.CharField(max_length=20)
    products = models.ManyToManyField(Product)
    baseFeature = models.ForeignKey(staticFeature, on_delete=models.CASCADE)

class ImageDynamicFeature(models.Model):

    featureImage = models.CharField(max_length=20)
    products = models.ManyToManyField(Product)
    baseFeature = models.ForeignKey(staticFeature, on_delete=models.CASCADE)


