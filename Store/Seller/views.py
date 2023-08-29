from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Product, productField
from .forms import product_detailform,productform

create = 0
update = 1

def add_new_product(cd):
    # Create a new product with provided data
    product = Product(name=cd['name'], price=cd['price'], quantity=cd['quantity'],product_quantity=cd['product_quantity'],image=cd['image'])
    

    return product

def update_product(cd,id):
    # Updta a new product with provided data
    product = Product.objects.get(id=id)
    product.name = cd["name"]
    product.price = cd["price"]
    product.quantity = cd["quantity"]
    product.product_quantity= cd["product_quantity"]
    product.image = cd["image"]
    product.save()
    return product

# Create your views here.
def seller_profile(request):

    return render(request,"sellerProfile.html")

def product_manager(request):

    return render(request,"productManager.html")

@login_required
def create_product(request):
    if request.method == 'POST':
        form = product_detailform(request.POST, request.FILES)

        if form.is_valid():
            print("terst")
            cd = form.cleaned_data
            product = add_new_product(cd)
            product.seller = request.user.seller
            product.save()
            return redirect('home')
    else:
        form = product_detailform()
    
    return render(request, "productDetail.html", {'form': form})
'''
@login_required
def update_product(request):
    if request.method == 'POST':
        form = product_detailform(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            product = update_product(cd,id)

            return redirect('productManager')
    else:
        form = product_detailform()
    return render(request, "productDetail.html", {'form': form})
'''

@login_required
def product_detail(request,type,id):

    if request.method == 'POST':

        if type == create:
        
            form = product_detailform(request.POST)

            if form.is_valid():
                cd = form.cleaned_data
                product = create_product(cd)

                return redirect('productManager')
       

        elif type == update:
            
            form = product_detailform(request.POST)

            if form.is_valid():
                cd = form.cleaned_data
                product = update_product(cd,id)

                return redirect('productManager')

        else:
            pass
        
    else:
        form = product_detailform()    

    return render(request, "productDetail.html", {'form': form})

def product_delete(request,id):

    product = Product.objects.get(id=id)
    product.delete()
    
    return redirect('productManager')
    

        