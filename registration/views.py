from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

from .models import CustomUser
from .forms import UserRegistrationForm, UserLoginForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('registration:login')  
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        print("a")
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            print(cd)
            if user is not None:
                auth_login(request, user)
                print("b")
                return redirect('main:index') 

            else:
                return render(request, 'registration/login.html', {'form': form, 'error': 'Неверный логин или пароль'})
        else: return render(request, 'registration/login.html', {'form': form, 'error': 'Неверный логин или пароль'})
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})

def get_user(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return HttpResponse({"user": True}, content_type='application/json')
        else:
            return None