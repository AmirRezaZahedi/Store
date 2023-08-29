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
    product.save()
    return product




@login_required
def seller_profile(request):

    return render(request,"sellerProfile.html")

@login_required
def product_manager(request):


    return render(request,"productManager.html")


@login_required
def create_product(request):
    if request.method == 'POST':
        form = product_detailform(request.POST, request.FILES)

        if form.is_valid():
         
            cd = form.cleaned_data
            product=Product()
            product.seller = request.user.seller
            product = update_product(cd)
        
            return redirect('home')
    else:
        form = product_detailform()
    
    return render(request, "productDetail.html", {'form': form})


@login_required
def update_product(request,id):
    if request.method == 'POST':
        form = product_detailform(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            product = Product.objects.get(id=id)
            product = update_product(cd,product)

            return redirect('productManager')
    else:
        product = Product.objects.get(id=id)
        form = product_detailform(instanse=product)

    return render(request, "productDetail.html", {'form': form})

@login_required
def delete_product(request,id):

    Product.objects.get(id=id).delete()
    
    return redirect('productManager')
    

        