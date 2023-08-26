from wsgiref import validate
from django.shortcuts import render,redirect



def home(request):

    return render(request,"home.html")

def customer_profile(request):

    return render(request,"customerProfile.html")

def seller_profile(request):

    return render(request,"sellerProfile.html")