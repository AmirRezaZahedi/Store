from pyexpat import features
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import *
from Accounts.models import User,Seller
from customer.models import Order 
from .forms import *
from .serializer import CategorySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import json

def update_product(cd,product):
    # Updta a new product with provided data
    
    product.name = cd["name"]
    product.price = cd["price"]
    product.quantity = cd["quantity"]
    product.product_quantity= cd["product_quantity"]

    category=product.category
    features=category.findRoot()

    
    


    product.image = cd["image"]

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

    return fields


@login_required
def seller_profile(request):

    return render(request,"Seller/sellerProfile.html")


@login_required
def product_manager(request):


    products =request.user.seller.product_set.all()

    return render(request,"Seller/productManager.html",{'products':products})


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


@login_required
def delete_product(request,id):

    Product.objects.get(id=id).delete()
    
    return redirect('productManager')
    

@login_required
def show_orders(request):

    orders =request.user.seller.order_set.all()

    return render(request, "Seller/orders.html", {'orders': orders})


@login_required
def create_product(request):
 
    if request.method == 'POST':
            
            cd = request.POST.copy()
            cd.update(request.FILES)

            product=Product()
            product.seller = request.user.seller

            category = Category.objects.get(id=cd["category"])
            product.category=category

            product = update_product(cd,product)
            product.save()

            response_data = {'message': 'محصول با موفقیت ایجاد شد.'}
            return JsonResponse(response_data, safe=False)
    else:
        pass
    
    return render(request, "Seller/createproduct.html")
        
class SetCategory(APIView):

    def post(self, request):
        try:
            data = json.loads(request.body.decode('utf-8'))
            category = data.get('category')

            # اطلاعات مدل "Category" را تبدیل به JSON کنید
            category_obj = Category.objects.get(categoryName=category)
            serializer = CategorySerializer(category_obj)
            serialized_data = serializer.data

            return Response(serialized_data, status=status.HTTP_200_OK)

        except json.JSONDecodeError:
            response_data = {'error': 'Invalid JSON data'}
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        # اطلاعات اولیه را تبدیل به JSON کنید
        categories = [
            {
                "product": [
                    {"digital": [["mobile", 5], ["TV", 6]]},
                    ["clothes", 3],
                    {"drink": [["water", 8], ["wine", 9], ["soda", 10]]}
                ]
            }
        ]
        return Response(categories, status=status.HTTP_200_OK)