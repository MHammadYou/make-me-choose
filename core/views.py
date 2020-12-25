from django.shortcuts import render

from polls.models import Poll as Poll_Model


def index(request):
    context = {
        'title': 'Make Me Choose',
        'polls': Poll_Model.objects.all()
    }

    return render(request, 'index.html', context)
