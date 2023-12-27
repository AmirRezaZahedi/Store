from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Cart , Order, Address
from Seller.models import Product , staticFeature,intDynamicFeature,ImageDynamicFeature,charDynamicFeature
from Accounts.models import User, Seller,Customer
from .forms import filterform,selectform,orderform,addressform
from django.contrib import messages
from .serializers import *
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAdminUser, IsAuthenticated




def query_by_filter(cd,request):

    products =Product.objects.all()
    return products

def customer_profile(request):
    
    return render(request, "customerProfile.html")

def home(request):
    
    return render(request,"customer/home.html")


def show_products(request):

    if request.method == 'POST':
        form = filterform(request.POST)

        if form.is_valid():

            cd = form.cleaned_data
            products=query_by_filter(cd,request)

            return render(request,"customer/products.html",{'products':products})
    else:
        cd=[]
        products=query_by_filter(cd,request)

    return render(request,"customer/products.html",{'products':products})


@login_required
def product_detail(request,id):

    form=selectform()
    product=Product.objects.get(id=id)
    
    return render(request, "customer/detail.html", {'product': product, 'form': form})



@login_required
def select(request,id):
    
    form = selectform(request.POST)
    if form.is_valid():

        cd=form.cleaned_data
        quantity=cd['quantity']

        product=Product.objects.get(id=id)
        cart=Cart()
        cart.customer=request.user.customer
        cart.product=product
        cart.quantity=quantity
        cart.save()

        return redirect('products')
    
    
@login_required
def show_cart(request):

    cart =request.user.customer.cart_set.all()
    total_price = 0
    for item in cart:
        total_price = total_price + item.product.price * item.quantity
    return render(request, "customer/cart.html", {'cart': cart, 'total_price': total_price})


@login_required
def update_cart(request, id):
    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        cart_item = Cart.objects.get(id=id)
        cart_item.quantity = quantity
        cart_item.save()
    return redirect('cart')


def order(cart,address):

    
    for item in cart:
        
        if item.product.quantity-item.quantity >= 0 :
            item.product.quantity-=item.quantity
            item.product.save()

        order=Order()
        order.customer=item.customer
        order.product=item.product
        order.quantity=item.quantity
        order.seller=item.product.seller
        order.address=address
        order.save()

        cart.delete()

    return redirect('cart')


@login_required
def show_orders(request):

    orders =request.user.customer.order_set.all()

    return render(request, "customer/orders.html", {'orders': orders})




@login_required
def delete_cart(request, id):

    cart = Cart.objects.get(id=id)
    cart.delete()
    return redirect('cart')

@login_required
def fill_address(request):
    
    if request.method == 'POST':
        
        form = addressform(request.POST)
        if form.is_valid():
            
            cd = form.cleaned_data
            addressUser = Address()
            addressUser.city = cd["city"]
            addressUser.address = cd["address"]
            addressUser.postcode = cd["postcode"]
            addressUser.save()
            cart =request.user.customer.cart_set.all()
            order(cart,addressUser)
            return redirect('customerOrders')
    else:
        form = addressform()

    return render(request, "customer/address.html", {'form':form})




