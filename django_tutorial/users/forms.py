#we can use this file to create custom forms
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
import os


class UserRegesterForm(UserCreationForm):
    email = forms.EmailField()

    #creates a nested namespace with configurations for the form
    class Meta:
        #model the form interacts with --> what model the data is inputed to
        model = User
        # fields that will be shown--> index determines order
        fields = ['username', 'email', 'password1', 'password2']

#model form
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image']