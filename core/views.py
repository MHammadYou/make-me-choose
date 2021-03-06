from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator

from polls.models import Poll as Poll_Model


def index(request):

    if request.method == 'POST' and request.POST.get('choice'):
        if request.user.is_authenticated:
            poll_obj = get_object_or_404(Poll_Model, pk=request.POST.get('id'))
            poll_obj.vote(request)
        else:
            messages.error(request, 'Please create an account to vote')
            return redirect('signup')

    polls = Poll_Model.objects.all().order_by('-id')
    polls_obj = Paginator(polls, 5)

    page_number = request.GET.get('page', '1')

    context = {
        'title': 'Make Me Choose',
        'polls': polls_obj.page(page_number)
    }
    return render(request, 'index.html', context)
