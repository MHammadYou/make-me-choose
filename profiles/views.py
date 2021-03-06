from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.core.paginator import Paginator

from polls.models import Poll as Poll_Model
from profiles.forms import UsernameUpdateForm, ProfileUpdateForm


@login_required
def profile(request):

    if request.method == 'POST' and request.POST.get('choice'):
        poll_obj = get_object_or_404(Poll_Model, pk=request.POST.get('id'))
        poll_obj.vote(request)
        return redirect('profile')

    polls = Poll_Model.objects.filter(author=request.user).all().order_by('-id')
    polls_obj = Paginator(polls, 5)
    page_number = request.GET.get('page', '1')

    context = {
        'title': 'Profile',
        'polls': polls_obj.page(page_number)
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
    profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

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
