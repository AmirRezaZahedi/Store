from wsgiref import validate
from django.shortcuts import render,redirect
from .models import User, Customer, Seller
from .forms import registerform, loginform, seller_registerform
from django.contrib.auth import authenticate, login as log, logout

def register_user(cd):
    user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
    user.first_name = cd['first_name']
    user.last_name = cd['last_name']
    user.save()
    return user

def register(request):
    if request.method == 'POST':
        form = registerform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            myuser = register_user(cd)
            myuser.access=1
            myuser.save()
            customer = Customer(user=myuser)
            customer.save()
            return redirect('login')
    else:
        form = registerform()

    return render(request, "register.html", {'form': form})

def seller_register(request):
    if request.method == 'POST':
        form = seller_registerform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            myuser = register_user(cd)
            myuser.access=0
            myuser.save()
            seller = Seller(user=myuser, store_name=cd['store_name'], store_type=cd['store_type'])
            seller.save()
            return redirect('login')
    else:
        form = seller_registerform()

    return render(request, "sellerRegister.html", {'form': form})


def login(request):
    
    if request.method =="POST":
        
        form=loginform(request.POST)   
        if form.is_valid():
            cd = form.cleaned_data
            
            user = authenticate(request, username=cd['username'],password=cd['password'])
            if user is not None:
                log(request, user)
                myuser=User.objects.get(username=cd['username'])
                if myuser.access == 1:
                    return redirect('home')
                else:
                    return redirect('sellerProfile')
            
    else:
        form=loginform()

    return render(request,"login.html",{'form':form})

def logout_view(request):
    logout(request)
    #messages.success(request, 'logout:)', 'success')
    return redirect('home')