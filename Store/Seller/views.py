from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Product, productField
from .forms import product_detailform


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
    form.initial['image']=product.image
    form.initial['price']=product.price
    form.initial['quantity']=product.quantity
    form.initial['product_quantity']=product.product_quantity

    return form




@login_required
def seller_profile(request):

    return render(request,"sellerProfile.html")


@login_required
def product_manager(request):

    products = Product.objects.all(id=request.user.seller.product.id)

    return render(request,"productManager.html",{'products':products})


@login_required
def create_product(request):
    if request.method == 'POST':
        form = product_detailform(request.POST, request.FILES)

        if form.is_valid():
         
            cd = form.cleaned_data
            product=Product()
            product.seller = request.user.seller
            product = update_product(cd,product)
        
            return redirect('home')
    else:
        form = product_detailform()
    
    return render(request, "productDetail.html", {'form': form})


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
        

    return render(request, "productDetail.html", {'form': form})


@login_required
def delete_product(request,id):

    Product.objects.get(id=id).delete()
    
    return redirect('productManager')
    

        