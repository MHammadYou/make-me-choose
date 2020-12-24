from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as login_user, logout as logout_user, authenticate
from django.contrib.auth.decorators import login_required

from .forms import LoginForm


def signup(request):
    form = UserCreationForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'title': 'Signup',
        'form': form
    }
    return render(request, 'users/signup.html', context)


def login(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():

            user = authenticate(request, **form.cleaned_data)
            if user:
                login_user(request, user)
                return redirect('profile')
            else:
                print("Invalid credentials!")

    context = {
        'title': 'Login',
        'form': form
    }

    return render(request, 'users/login.html', context)


def logout(request):
    logout_user(request)
    return render(request, 'users/logout.html', {'title': 'Logout'})


@login_required
def profile(request):
    return render(request, 'users/profile.html', {'title': 'Profile'})
