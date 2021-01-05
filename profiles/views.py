from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

from polls.models import Poll as Poll_Model


@login_required
def profile(request):
    polls = Poll_Model.objects.filter(author=request.user).all()

    context = {
        'title': 'Profile',
        'polls': polls
    }
    print(polls)

    return render(request, 'profiles/profile.html', context)


@login_required
def change_password(request):
    form = PasswordChangeForm(request.user)

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated. You can login with new password')
            return redirect('login')

    context = {
        'title': 'Change Password',
        'form': form
    }

    return render(request, 'profiles/change_password.html', context)
