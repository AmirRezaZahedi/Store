# Import necessary modules and models
from ast import Not
from django.contrib.auth import authenticate, login as log, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import User, Customer, Seller
from .forms import registerform, seller_registerform, loginform
from django.http import JsonResponse


def login(request):
    if request.method == "POST":
        # Process the login form data
        form = loginform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            # Authenticate user`    `
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                # Log the user in
                log(request, user)
                if user.access == 1:
                    pass
                    # Redirect to home page for customers
                    #return redirect('home')
                else:
                    return JsonResponse({'A':'B'})
                    # Redirect to seller profile for sellers
                    #return redirect('sellerProfile')
    else:
        # Display an empty login form
        form = loginform()

    return render(request, "Accounts/login.html", {'form': form})


@login_required
def logout_view(request):
    # Log the user out
    logout(request)
    # Redirect to home page after logout
    return redirect('home')
