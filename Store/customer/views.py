from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Product, productField
from Accounts.models import User, Seller
from .forms import filterform

def query_by_filter(cd,request):
    products =request.user.seller.product_set.all()
    return products


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
     
    
    return render(request,"Seller/productManager.html",{'product':product})


@login_required
def order(request,id):

    Product.objects.get(id=id).delete()
    
    return redirect('productManager')
