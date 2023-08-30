from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Cart 
from Seller.models import Product , productField
from Accounts.models import User, Seller
from .forms import filterform,orderform

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

    form=orderform()
    product=Product.objects.get(id=id)
    
    return render(request, "customer/detail.html", {'product': product, 'form': form})



@login_required
def order(request,id):
    print("hello")

    form = orderform(request.POST)
    cd = form.cleaned_data
    number=cd['number']

    product=Product.objects.get(id=id)
    cart=Cart()
    cart.customer=request.user.customer
    cart.product=product
    cart.number=number
    cart.save()
    return redirect('products')
    

def show_cart(request):

    cart =request.user.customer.cart_set.all()

    return render(request, "customer/cart.html", {'cart': cart})

