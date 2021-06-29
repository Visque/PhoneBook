from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.
def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)                   #authenticate() returns None if wrong credentials
        if user is not None:                                                        # Correct credentials
            login(request, user)
            anonymous = False
            return redirect("/")                                      
        else:                                                                       # Wrong credentials
            anonymous = True
            return render(request, 'pages/login.html', {'anonymous': anonymous})                                           
    return render(request, 'pages/login.html')

def logoutuser(request):
    logout(request)
    return redirect("/accounts/login")

def registeruser(request):
    if request.method =="POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(first_name = fname, last_name = lname, username = username, email=email, password=password)
        user.save()
        registerFlag = True
        return render(request, 'pages/login.html', {'registerFlag': registerFlag})
    registerFlag = False
    return render(request, 'pages/register.html')