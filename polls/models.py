from django.db import models

from django.contrib.auth.models import User

poll_type_choices = [
    ('text', 'text'),
    ('image', 'image')
]


class Poll(models.Model):
    title = models.CharField(max_length=255, blank=False)
    option_1 = models.CharField(max_length=255, blank=False)
    count_1 = models.PositiveIntegerField(default=0)
    option_2 = models.CharField(max_length=255, blank=False)
    count_2 = models.PositiveIntegerField(default=0)
    poll_type = models.CharField(max_length=5, choices=poll_type_choices, default='text')
    ended = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    voters = models.ManyToManyField(User, related_name='voters')

    def __str__(self):
        return self.title[:50]
