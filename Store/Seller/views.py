from dataclasses import Field
from pyexpat import features
from PIL import Image
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import *
from Accounts.models import User,Seller
from customer.models import Order 
from .forms import *
from .serializers import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
import json

from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAdminUser, IsAuthenticated


def update_product(cd,product):
    # Updta a new product with provided data
    
    #product.name = cd["name"]
    product.name = "mobile"
    #product.price = cd["price"]
    product.price = 580
    #product.quantity = cd["quantity"]
    product.quantity = 8
    #product.product_quantity= cd["product_quantity"]
    product.product_quantity=0
    

    category=product.category
    features = category.findRoot()
    fields = []
    fields = staticFeature.findFields(features,fields)

    features=[]
    
    for field in fields:

        typeField=0

        if(field.featureName not in cd):return False
        
        intField=field.staticfeature_set.filter(featureName="intField")
        if intField.exists():typeField=intField[0].id

        else:
            charField=field.staticfeature_set.filter(featureName="charField")
            if charField.exists():typeField=charField[0].id

            else:
                imageField=field.staticfeature_set.filter(featureName="imageField")
                if imageField.exists():typeField=imageField[0].id
                else:return False

        
        Type = type(cd[field.featureName])

        if Type is int and typeField == 9:

            feature=intDynamicFeature()
            feature.featureNumber=cd[field.featureName]
            feature.baseFeature=field

        elif Type is str and typeField == 8: 

            feature=charDynamicFeature()
            feature.featureName=cd[field.featureName]
            feature.baseFeature=field

        elif Type is Image.Image and typeField == 7:  
            feature=ImageDynamicFeature()
            feature.featureImage=cd[field.featureName]
            feature.baseFeature=field

        else:return False

        #feature.products.add(product)
        features.append(feature)
    product.save()    
    for feature in features:
        feature.save()
        feature.products.add(product)

    return product

'''
def fill_form(request,product):
    form = product_detailform()

    form.initial['name']=product.name
    form.initial['price']=product.price
    form.initial['quantity']=product.quantity
    form.initial['product_quantity']=product.product_quantity

    form.initial['image']=product.image

    return form
'''
def get_fields(category):
    
    #choices=["تعدادی","کیلویی"]

    #fields = [["price","quantity"],["name"],[],["kilogram"]]

    
    features = category.findRoot()
    fields = []
    fields = staticFeature.findFields(features,fields)

    return fields


@login_required
def seller_profile(request):

    return render(request,"Seller/sellerProfile.html")


class OrdersViewSet(ModelViewSet):
    
    serializer_class = OrdersSerializer
    
    def get_queryset(self):
        
        user=self.request.user
        products=user.seller.order_set.all()
        return products


class ProductViewSet(ModelViewSet):

    serializer_class=  ProductSerializer  
    '''
    def create(self):
            
        #cd = request.POST.copy()
        #cd.update(request.FILES)
        cd = self.request.data

        product=Product()
        product.seller = self.request.user.seller

        category = Category.objects.get(id=cd["category"])
        product.category=category

        product = update_product(cd,product)
        if(product==False):
            return JsonResponse({'message': 'created product failed..!'})

        #product.save()

        return JsonResponse({'message': 'create product successfull'})
    '''
    #def get_queryset(self):
        
    #    user=self.request.user
    #    products=user.seller.product_set.all()
    #    return products
    def get_queryset(self):
        return Product.objects.all()
    #def get_serializer_context(self):
    #    return {'seller_id': self.request.seller}

class FieldsViewSet(ReadOnlyModelViewSet):
    
    
    serializer_class = FieldsSerializer
    
    
    def get_queryset(self):
        category = Category.objects.get(id=self.kwargs['category_pk'])

        fields=get_fields(category)
        
        return fields 
      

class CategoryViewSet(ReadOnlyModelViewSet):
    queryset=Category.objects.filter(id=1)
    serializer_class = CategorySerializer
