from wsgiref import validate
from django.shortcuts import render,redirect
from .models import users
from .forms import registerform


def register(request):

    
    if request.method =="POST":
        
        form=registerform(request.POST)   
        if form.is_valid():
            form.save()
            
            return redirect('login')

    else:
        form=registerform()

    return render(request,"register.html",{'form':form})

def login(request):

    
    if request.method =="POST":
        
        form=registerform(request.POST)   
        if form.is_valid():
            form.save()
            
            return redirect('login')

    else:
        form=registerform()

    return render(request,"register.html",{'form':form})

