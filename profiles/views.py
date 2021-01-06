from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

from polls.models import Poll as Poll_Model
from profiles.forms import UsernameUpdateForm, ProfileUpdateForm


@login_required
def profile(request):
    polls = Poll_Model.objects.filter(author=request.user).all()

    context = {
        'title': 'Profile',
        'polls': polls
    }

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


@login_required
def edit_profile(request):

    user_form = UsernameUpdateForm(request.POST or None, instance=request.user)
    profile_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.profile)

    if request.method == 'POST':
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile')

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'profiles/edit_profile.html', context)
