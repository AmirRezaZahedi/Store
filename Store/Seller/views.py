from django.shortcuts import render,redirect
from .models import Product, productField
from .forms import product_detailform,productform

create=0
update=1

def create_product(cd):
    # Create a new product with provided data
    product = Product(name=cd['name'], price=cd['price'], quantity=cd['quantity'],product_quantity=cd['product_quantity'],image=cd['image'])
    
    product.save()
    return product

def update_product(cd,id):
    # Updta a new product with provided data
    product = Product.objects.get(id=id)
    
    product.save()
    return product

# Create your views here.
def seller_profile(request):

    return render(request,"sellerProfile.html")

def product_manager(request):

    return render(request,"productManager")


def product_detail(request,type,id):

    if request.method == 'POST':

        if type==create:
        
            form = product_detailform(request.POST)

            if form.is_valid():
                cd=form.cleaned_data
                product=create_product(cd)

                return redirect('productManager')
       

        elif type==update:
            
            form = product_detailform(request.POST)

            if form.is_valid():
                cd=form.cleaned_data
                product=update_product(cd,id)

                return redirect('productManager')

        else:
            pass
        
    else:
        form = product_detailform()    

    return render(request, "productDetail.html", {'form': form})

def product_delete(request,id):
    
    return redirect('productManager')
    

        