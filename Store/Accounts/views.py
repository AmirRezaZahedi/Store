# Import necessary modules and models
from ast import Not
from django.contrib.auth import authenticate, login as log, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import User, Customer, Seller
from .forms import registerform, seller_registerform, loginform

# User registration function
def register_user(cd):
    # Create a new user with provided data
    user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
    user.first_name = cd['first_name']
    user.last_name = cd['last_name']
    user.save()
    return user

# User registration view
def register(request):
    if request.method == 'POST':
        # Process the registration form data
        form = registerform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # Register the user
            myuser = register_user(cd)
            myuser.access = 1
            myuser.save()
            # Create a Customer instance
            customer = Customer(user=myuser)
            customer.save()
            # Redirect to login page
            return redirect('login')
    else:
        # Display an empty registration form
        form = registerform()

    return render(request, "customerRegister.html", {'form': form})

# Seller registration view
def seller_register(request):
    if request.method == 'POST':
        # Process the seller registration form data
        form = seller_registerform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # Register the seller user
            myuser = register_user(cd)
            myuser.access = 0
            myuser.save()
            # Create a Seller instance
            seller = Seller(user=myuser, store_name=cd['store_name'], store_type=cd['store_type'])
            seller.save()
            # Redirect to login page
            return redirect('login')
    else:
        # Display an empty seller registration form
        form = seller_registerform()

    return render(request, "sellerRegister.html", {'form': form})


def login(request):
    if request.method == "POST":
        # Process the login form data
        form = loginform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            # Authenticate user
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                # Log the user in
                log(request, user)
                if user.access == 1:
                    # Redirect to home page for customers
                    return redirect('home')
                else:
                    # Redirect to seller profile for sellers
                    return redirect('sellerProfile')
    else:
        # Display an empty login form
        form = loginform()

    return render(request, "login.html", {'form': form})


@login_required
def logout_view(request):
    # Log the user out
    logout(request)
    # Redirect to home page after logout
    return redirect('home')
