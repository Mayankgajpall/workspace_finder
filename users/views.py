from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.

def log_reg(request):
    return render(request, 'users/login_register.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        fullname = request.POST['fullname']
        email = request.POST['email']
        password = request.POST['password']
        mobile = request.POST['mobile']
        companyname = request.POST['cname']
        fname,lname=fullname.split(" ")
        user = User.objects.create_user(username=username, email=email, password=password, first_name=fname, last_name=lname)
        pro = Profile(user=user,company_name=companyname, mobile=mobile)
        pro.save()
        messages.success(request, "Registered successfully. Please Login")
        return redirect('login_register_page')
    else:
        messages.warning(request, "Error occurred. Please Try Again")
        return redirect('login_register_page')

def auth_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.POST.get('next'):
                return redirect(request.POST.get('next'))
            else:
                message = " {0} Logged In Successfully".format(username)
                messages.success(request, message)
                return redirect('home')
        else:
            messages.warning(request, "Invalid Credentials. Please Try Again")
            return redirect('login_register_page')  

def user_logout(request):
    logout(request)
    messages.success(request, "Logged Out successfully")
    return redirect('home')