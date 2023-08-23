from wsgiref import validate
from django.shortcuts import render,redirect
from .models import users
from .forms import registerform, loginform
from django.contrib.auth import authenticate, login, logout

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
        
        form=loginform(request.POST)   
        if form.is_valid():
            credentials = form.cleaned_data
            user = authenticate(username=credentials['user_name'],
                            password=credentials['password'])
            if user:
                login(request, user)
                return redirect('register')
            
            return redirect('login')

    else:
        form=loginform()

    return render(request,"register.html",{'form':form})

