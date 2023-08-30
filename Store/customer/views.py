from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Cart 
from Seller.models import Product , productField
from Accounts.models import User, Seller
from .forms import filterform

def query_by_filter(cd,request):
    products =request.user.seller.product_set.all()
    return products

def customer_profile(request):
    pass
def home(request):
    pass

@login_required
def show_products(request):

    if request.method == 'POST':
        form = filterform(request.POST)

        if form.is_valid():
         
            cd = form.cleaned_data

            products=query_by_filter(cd,request)
            return render(request,"Seller/productManager.html",{'products':products})
    
    cd=[]
    products=query_by_filter(cd,request)

    return render(request,"Seller/productManager.html",{'products':products})


@login_required
def product_detail(request,id):

    product=Product.objects.get(id=id)
    
    return render(request,"Seller/productManager.html",{'product':product})


@login_required
def order(request,id,number):

    product=Product.objects.get(id=id)
    cart=Cart()
    cart.customer=request.user.customer
    cart.product=product
    cart.number=number
    
    return redirect('productManager')
