from django.shortcuts import render,redirect
from .models import Product, productField
from .forms import product_detailform,productform

create=1
update=2

def create_product(cd):
    # Create a new product with provided data
    product = Product(cd['username'], cd['email'], cd['password'])
    product.first_name = cd['first_name']
    product.last_name = cd['last_name']
    product.save()
    return product

# Create your views here.
def seller_profile(request):

    return render(request,"sellerProfile.html")

def products_panel(request):

    return render(request,"productsPanel.html")


def product_detail(request,type,id):

    if request.method == 'POST':

        if type==create:
        
            
            form = product_detailform(request.POST)

            if form.is_valid():
                
                return redirect('productDetail')
       

        elif type==update:

        
            
            form = product_detailform(request.POST)

            if form.is_valid():
                
                return redirect('productDetail')

        else:
            pass
        
    else:
        form = product_detailform()    

    return render(request, "productDetail.html", {'form': form})

def product_delete(request,type,id):

    
    if type==delete:
        if request.method == 'POST':
            
            form = product_detailform(request.POST)

            if form.is_valid():
                
                return redirect('productDetail')
        else:
            
            form = product_detailform()

            return render(request, "productDetail.html", {'form': form})
    

        