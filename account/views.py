from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email= request.POST['email']
        username= request.POST['username']
        password= request.POST['password']
        password2= request.POST['password2']
        
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'User already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email already exists')
                    return redirect('register')
                else:
                    form=User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password , username=username)
                    form.save()
                    messages.success(request,'User registration successful')
                    return redirect('signin')
        else:
            messages.error(request, 'password does not match')
            return redirect('register')
    return render(request, 'register.html')


def signin(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']  
        
        user= authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'signin.html')

def dashboard(request):
    return render(request, 'dashboard.html')


def signout(request):
    logout(request)
    return redirect('signin')
    
