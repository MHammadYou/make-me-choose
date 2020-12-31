# from django.db.models.signals import m2m_changed
# from django.contrib.auth.models import User
# from django.dispatch import receiver
#
# from .models import PollVoters
#
#
# @receiver(m2m_changed, sender=User)
# def create_poll_voters(sender, instance, created, **kwargs):
#     if created:
#         PollVoters.objects.create(user=instance)
