from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib import messages
from django.core.exceptions import ValidationError 
from django.contrib.auth import  authenticate , login, logout
    # User is authenticated
# Create your views here.
from . forms import UserFormRegister
from . forms import AdressFormUser
def auths(request):
    if request.method == 'POST':
        form = UserFormRegister(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
            messages.success(request, 'your is creating ')
            
    else:
        form = UserFormRegister        
    return render(request, 'sinup.html', {'form': form})  

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user :
            login(request, user)
            return redirect('index')
            messages.success(request, 'vous bien connecté')
    else:
        messages.error(request, 'username or password is define ')        
    
    return render(request, 'login.html')


def user_logout(request):
     logout(request)
     return redirect('index')
 
def checkout(request):
   
    if request.method == 'POST':
        form= AdressFormUser(request.POST)
        if form.is_valid():
            form = form.save()
            return redirect('index')
    else:
        form= AdressFormUser()
   
        
            
    return render(request, 'checkout.html', {'form': form}) 
     