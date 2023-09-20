from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Product,staticFeature,intDynamicFeature,charDynamicFeature,ImageDynamicFeature
from Accounts.models import User, Seller
from customer.models import Order 
from .forms import *
import json

def update_product(cd,product):
    # Updta a new product with provided data
    
    product.name = cd["name"]
    product.price = cd["price"]
    product.quantity = cd["quantity"]
    product.product_quantity= cd["product_quantity"]


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

    fields = [["price",0],["quantity",0],["name",1],["image",2],["product_quantity",3,choices]]

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
            product = update_product(cd,product)
            product.save()

            response_data = {'message': 'محصول با موفقیت ایجاد شد.'}
            return JsonResponse(response_data, safe=False)
    else:
        pass
    
    return render(request, "Seller/createproduct.html")
        
def set_category(request):

    if request.method == 'POST':

        try:
            data = json.loads(request.body.decode('utf-8'))  # Parse JSON data from request body
            category = data.get('category')

            felieds = get_fields(category)
            
            return JsonResponse(felieds, safe=False)
    
        except json.JSONDecodeError:
            response_data = {'error': 'Invalid JSON data'}
            return JsonResponse(response_data, status=400)  # Return a 400 Bad Request status for invalid JSON
        
    else:

        categories = [
            {
                "product": [
                    {"digital": [["mobile",4], ["TV",5]]},
                    ["clothes",2],
                    {"drink": [["water",6], ["wine",7], ["soda",8]]}
                ]
            }
        ]
        return JsonResponse(categories, safe=False)