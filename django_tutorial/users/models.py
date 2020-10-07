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
    # this line allows us to create custom filederedtorys for each instance of a inhereted model
    def make_user_dir(instance, filename):
        return f'images/profile_pics/{instance.user.username}/{filename}'
    # this is what lets us acctual upload the image    
    profile_image = models.ImageField(default='defult.jpg', upload_to=make_user_dir)

    #dudner str mentod 
    def __str__(self):
        return f'{self.user.username}'

      