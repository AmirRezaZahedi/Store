from django.shortcuts import render
from .models import users
from .forms import registerform


def register(request):
    if request.method =="POST":
        pass
    else:
        form=registerform()

    return render(request,"register.html",{'form':form})