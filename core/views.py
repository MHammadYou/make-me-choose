from django.shortcuts import render

from polls.models import Poll as Poll_Model


def index(request):

    if request.method == 'POST':
        poll_data = request.POST
        poll_obj = Poll_Model.objects.filter(id=poll_data.get('id')).first()

        if poll_data.get('choice') == poll_obj.option_1:
            poll_obj.count_1 += 1
        else:
            poll_obj.count_2 += 1
        poll_obj.save()

    context = {
        'title': 'Make Me Choose',
        'polls': Poll_Model.objects.all()
    }

    return render(request, 'index.html', context)
