from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def login(request) :
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists() :
            user = auth.authenticate(username=username, password=password)
            if user :
                auth.login(request, user)
                print('login succes')
                return redirect('/')
            else:
                messages.info(request, 'wrong password')
                return redirect('login')    
        else :
            messages.info(request, 'user not found')
            return redirect('login')

    else :
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already exist')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exist')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                user.save()                
                return redirect('login')
        else:
            messages.info(request, 'password not matched')
            return redirect('register')
    else:
        return render(request, 'register.html')

def logout(request) :
    auth.logout(request)
    return redirect('/')