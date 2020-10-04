# signal that is fired when post is saved
from django.db.models.signals import post_save
#sender 
from django.contrib.auth.models import User
#reciver
from django.dispatch import receiver
# profile model
from .models import Profile

# this creates a new profile for a new user on user creation
# reciver
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# save porfiles
@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()

# to make this work we have to add the signal to the users.apps.py file