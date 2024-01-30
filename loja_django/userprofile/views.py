from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Userprofile



def vendor_details(request):

    return render(request,'userprofile/vendor_details.html')

def my_account(request):
    
    return render(request,'userprofile/myaccount.html')

def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            login(request,user)
            userprofile = Userprofile.objects.create(user=user)
            
            return redirect('frontpage')
        
    else:
        form = UserCreationForm()
        
    return render(request,'userprofile/register.html', {'form':form})