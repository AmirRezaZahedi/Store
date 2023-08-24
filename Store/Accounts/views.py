from wsgiref import validate
from django.shortcuts import render,redirect
from .models import User
from .forms import registerform, loginform
from django.contrib.auth import authenticate, login as log, logout

def register(request):

    if request.method == 'POST':
        form = registerform(request.POST)
        if form.is_valid():
                cd = form.cleaned_data
                User = User.objects.create_User(cd['Username'], cd['email'], cd['password'])
                User.first_name = cd['first_name']
                User.last_name = cd['last_name']
                User.save()
                return redirect('login')
    else:
        form = registerform()
    return render(request,"register.html",{'form':form})

def login(request):

    
    if request.method =="POST":
        
        form=loginform(request.POST)   
        if form.is_valid():
            credentials = form.cleaned_data
            User = authenticate(request, Username=credentials['Username'],password=credentials['password'])
            if User is not None:
                    log(request, User)
                    return redirect('register')
            
        return redirect('login')

    else:
        form=loginform()

    return render(request,"register.html",{'form':form})

