from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.models import User

def register(request):

    context = {}
    if request.method=="POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        repidpassword = request.POST.get("repidpassword")

        if len(password) >= 4:
            if password == repidpassword:
                try:
                    User.objects.create_user(username=username, password=password, 
                    first_name=firstname, last_name=lastname, email=email)
                    return redirect('auth')
                except IntegrityError:
                    context['error'] = 'Користувач вже існує'
                    
            else:
                context['error'] = 'Пароль не правильний'
        else:
            context['error'] = 'Пароль повинен мати більше 4 символів'
    return render(request, 'main/register.html', context=context)

def auth(request):
    context = {}
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('main')
        else:
            context['error'] = 'Не правильний логін або пароль'
    return render(request, 'main/autenfication.html',context=context)


def logoutuser(request):
    logout(request)
    return redirect('main')
# Create your views here.
