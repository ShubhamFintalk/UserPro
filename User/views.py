from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout

from .models import Posts


def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'create.htm')


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('password')
        print(username, password)

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('/login')


def signUp(request):
    if request.method == 'POST':
        fname_sign = request.POST['fname_sign']
        lname_sign = request.POST['lname_sign']
        email_sign = request.POST['email_sign']
        user_sign = request.POST['user_sign']
        password_sign = request.POST['password_sign']
        # check for erroneous inputs

        # create user
        myuser = User.objects.create_user(user_sign, email_sign, password_sign)
        myuser.first_name = fname_sign
        myuser.last_name = lname_sign
        myuser.save()
        messages.success(request, "Your account has been Created, Enjoy !! ")
        return redirect('/login')
    else:
        return HttpResponse('404 - NOT FOUND ')


def posts(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        text = request.POST.get('text')
        # user_id = User.objects.get(user.userName=username)
        mypost = Posts(user=username, text=text)
        mypost.save()
        return redirect('/login')
    else:
        return HttpResponse('404 - NOT FOUND ')
    # else:
    #     userN = User.objects.all().order_by('userName')
    #     return render(request, 'create.htm', {'usernames': userN})
