from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Cart , Order
from Seller.models import Product , productField
from Accounts.models import User, Seller
from .forms import filterform,selectform,orderform
from django.contrib import messages

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

        messages.success(request, 'successfully', 'success')
        return redirect('products')
    
    
@login_required
def show_cart(request):

    cart =request.user.customer.cart_set.all()
    total_price = 0
    for item in cart:
        total_price = total_price + item.product.price * item.quantity
    return render(request, "customer/cart.html", {'cart': cart, 'total_price': total_price})


@login_required
def order(request):

    cart =request.user.customer.cart_set.all()
    for item in cart:
        order=Order()
        order.customer=item.customer
        order.product=item.product
        order.quantity=item.quantity
        order.seller=item.product.seller
        order.save()
        cart.delete()

    return redirect('cart')


@login_required
def show_orders(request):

    orders =request.user.customer.order_set.all()

    return render(request, "customer/orders.html", {'orders': orders})