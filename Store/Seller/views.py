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
from .serializer import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
import json

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

def fill_form(request,product):
    form = product_detailform()

    form.initial['name']=product.name
    form.initial['price']=product.price
    form.initial['quantity']=product.quantity
    form.initial['product_quantity']=product.product_quantity

    form.initial['image']=product.image

    return form

def get_fields(category):
    
    choices=["تعدادی","کیلویی"]

    fields = [["price","quantity"],["name"],[],["kilogram"]]

    
    features = category.findRoot()
    fields = []
    fields = staticFeature.findFields(features,fields)

    return fields


@login_required
def seller_profile(request):

    return render(request,"Seller/sellerProfile.html")



class ProductManager(APIView):
    def post(self, request):
        pass

    def get(self, request):

        products = request.user.seller.product_set.all()
        serialized_data = ProductSerializer(products, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)
        #return render(request,"Seller/productManager.html",{'products':products})


@login_required
def update_Product(request,id):
    if request.method == 'POST':
        form = product_detailform(request.POST,request.FILES)
        
        if form.is_valid():
            
            cd = form.cleaned_data
            product = Product.objects.get(id=id)
            product = update_product(cd,product)
            product.save()
            return redirect('productManager')
    else:
        product = Product.objects.get(id=id)
        
        form=fill_form(request,product)
        

    return render(request, "Seller/productDetail.html", {'form': form})



def delete_product(request,id):

    Product.objects.get(id=id).delete()
    
    return redirect('productManager')
    


class ShowOrders(APIView):
    
    def post(self,request):

        pass 

    def get(self,request):
        
        orders =request.user.seller.order_set.all()
        serializer = OrdersSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #return render(request, "Seller/orders.html", {'orders': orders})



class CreateProduct(APIView):
 
    def post(self, request):
            
        #cd = request.POST.copy()
        #cd.update(request.FILES)
        cd = request.data

        product=Product()
        product.seller = request.user.seller

        category = Category.objects.get(id=cd["category"])
        product.category=category

        product = update_product(cd,product)
        if(product==False):
            return JsonResponse({'message': 'created product failed..!'})

        #product.save()

        return JsonResponse({'message': 'create product successfull'})
        
    
    def get(self, request):

        response_data = {'error': 'get not suported..!'}
        return Response(response_data, status=status.HTTP_404_NOT_FOUND)

    #return render(request, "Seller/createproduct.html")
        

class SetCategory(APIView):

    def post(self, request):
        try:
            data = json.loads(request.body.decode('utf-8'))
            category = Category.objects.get(id=data['category'])

            fields=get_fields(category)
            serialized_data = FieldsSerializer(fields, many=True).data

            return Response(serialized_data, status=status.HTTP_200_OK)

        except json.JSONDecodeError:

            response_data = {'error': 'Invalid JSON data'}
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):

        try:
            productCategory = Category.objects.get(id=1)
            serializer = CategorySerializer(productCategory)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Category.DoesNotExist:
            response_data = {'error': 'Category not found'}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

