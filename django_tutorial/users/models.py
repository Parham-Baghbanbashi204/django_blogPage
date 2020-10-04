from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    #creates a one to one relationship with the user
    #on_delete tells django what to do when a user is deleted
    # cascade = if user is deleted delete the profile, works only one way
    # becuse we have made a one to one relationship we have accsess to the user fields, and we can now add fields to user
    # through profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # allows us to upload images
    profile_image = models.ImageField(default='defult.jpg', upload_to=f'images/profile_pics')

    #dudner str mentod 
    def __str__(self):
        return f'{self.user.username}'

      