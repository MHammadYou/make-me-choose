from django.shortcuts import render
from django.contrib import messages

from polls.models import Poll as Poll_Model


def index(request):
    if request.method == 'POST':

        if request.user.username:
            poll_data = request.POST
            poll_obj = Poll_Model.objects.filter(id=poll_data.get('id')).first()

            if request.user in poll_obj.voters.all():
                messages.error(request, 'You can only vote once')
            else:
                if poll_data.get('choice') == poll_obj.option_1:
                    poll_obj.count_1 += 1
                else:
                    poll_obj.count_2 += 1
                poll_obj.voters.add(request.user)
                poll_obj.save()
                messages.success(request, 'Voted Successfully')
        else:
            messages.error(request, 'Please login to vote')

    context = {
        'title': 'Make Me Choose',
        'polls': Poll_Model.objects.all()
    }

    return render(request, 'index.html', context)
