from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import PollForm
from .models import Poll as Poll_Model


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
