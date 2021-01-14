from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login as login_user, logout as logout_user, authenticate
from django.contrib import messages

from .forms import LoginForm

from polls.models import Poll as Poll_Model


def signup(request):

    if request.user.is_authenticated:
        return redirect('index')

    form = UserCreationForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created. You can login now")
            return redirect('login')

    context = {
        'title': 'Signup',
        'form': form
    }
    return render(request, 'users/signup.html', context)


def login(request):

    if request.user.is_authenticated:
        return redirect('index')

    form = LoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():

            user = authenticate(request, **form.cleaned_data)
            if user:
                login_user(request, user)
                messages.success(request, 'You have been logged in')
                return redirect('index')
            else:
                messages.error(request, 'Invalid Credentials')

    context = {
        'title': 'Login',
        'form': form
    }

    return render(request, 'users/login.html', context)


def logout(request):
    logout_user(request)
    messages.success(request, "Logged out")
    return render(request, 'users/logout.html', {'title': 'Logout'})


def users(request, id):
    user = get_object_or_404(User, pk=id)

    if user == request.user:
        return redirect('profile')

    polls = get_list_or_404(Poll_Model, author=user)

    if request.method == 'POST':
        print(request.POST.get('choice'))
        if request.POST.get('choice'):
            if request.user.is_authenticated:
                poll_obj = get_object_or_404(Poll_Model, pk=request.POST.get('id'))
                poll_obj.vote(request)
                # return redirect('users')
            else:
                messages.error(request, 'Please create an account to vote')


    context = {
        'title': f"{user.username}'s Profile",
        'user_': user,
        'polls': polls
    }

    return render(request, 'users/users.html', context)
