from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import PollForm, PollImgForm
from .models import Poll as Poll_Model


@login_required
def poll_type(request):
    return render(request, 'polls/poll_type.html', {})


@login_required
def new_poll(request):
    form = PollForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            Poll_Model.objects.create(**form.cleaned_data, author=request.user)
            return redirect('index')

    context = {
        'title': 'Create New Poll',
        'form': form
    }

    return render(request, 'polls/new-poll.html', context)


@login_required
def new_img_poll(request):
    form = PollImgForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            Poll_Model.objects.create(**form.cleaned_data, author=request.user)
            messages.success(request, 'Poll Added')
            return redirect('index')

    context = {
        'title': 'Create Poll',
        'form': form
    }

    return render(request, 'polls/new-poll.html', context)


def edit_poll(request, id):

    poll = get_object_or_404(Poll_Model, pk=id)

    if poll.author == request.user:

        form = PollForm(
            request.POST or None,
            initial={
                'title': poll.title,
                'option_1': poll.option_1,
                'option_2': poll.option_2
            }
        )

        if request.method == 'POST':
            if form.is_valid():
                poll.title = form.cleaned_data.get('title')
                poll.option_1 = form.cleaned_data.get('option_1')
                poll.option_2 = form.cleaned_data.get('option_2')
                poll.save()
                messages.success(request, 'Poll Updated')
                return redirect('index')
    else:
        raise Http404('Forbidden')

    context = {
        'title': 'Update Poll',
        'form': form
    }

    return render(request, 'polls/edit_poll.html', context)


def delete_poll(request, id):
    poll = get_object_or_404(Poll_Model, pk=id)

    if poll.author == request.user:
        poll.delete()
        messages.success(request, 'Poll Deleted')
        return redirect('index')
    else:
        raise Http404('Forbidden')


def end_poll(request, id):
    poll = get_object_or_404(Poll_Model, pk=id)

    if poll.author == request.user:
        poll.ended = True
        poll.save()
        return redirect('index')
    else:
        raise Http404('Forbidden')
