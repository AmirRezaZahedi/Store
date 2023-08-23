from wsgiref import validate
from django.shortcuts import render,redirect
from .models import users
from .forms import registerform


def register(request):

    
    if request.method =="POST":
        user=users.objects.create()
        form=registerform(request.POST,instance=user)   
        if form.is_valid():
            form.save()
            form2=registerform()
            return render(request,"register.html",{'form':form2})

    else:
        form=registerform()

    return render(request,"register.html",{'form':form})

