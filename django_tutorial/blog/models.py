from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # forignkey creates working realationship between user and post tables in relational database
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # dunder str method --> displays information when we print the class
    def __str__(self):
    	return self.title

    # Redirect URL for class based views
    # allows django to find the location of a specific post
    # reverse displays url as string rederct redirects you to the view
    def get_absolute_url(self):
        return reverse('post-detail', kwargs=({'pk':self.pk}))