from django.db import models
from django.contrib import messages

from django.contrib.auth.models import User

poll_type_choices = [
    ('text', 'text'),
    ('image', 'image')
]


class Poll(models.Model):
    title = models.CharField(max_length=255, blank=False)
    option_1 = models.CharField(max_length=255, blank=True)
    image_1 = models.ImageField(upload_to='poll_images', blank=True)
    count_1 = models.PositiveIntegerField(default=0)
    option_2 = models.CharField(max_length=255, blank=True)
    image_2 = models.ImageField(upload_to='poll_images', blank=True)
    count_2 = models.PositiveIntegerField(default=0)
    poll_type = models.CharField(max_length=5, choices=poll_type_choices, default='text')
    ended = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    voters = models.ManyToManyField(User, related_name='voters')

    def vote(self, request):

        form_data = request.POST

        if request.user in self.voters.all():
            messages.error(request, 'You can only vote once')
        else:
            if form_data.get('choice') == self.option_1:
                self.count_1 += 1
            else:
                self.count_2 += 1
            self.voters.add(request.user)
            self.save()
            messages.success(request, 'Voted Successfully')

    def __str__(self):
        return self.title[:50]
