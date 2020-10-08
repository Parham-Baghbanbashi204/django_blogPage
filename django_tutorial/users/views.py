from django.shortcuts import render, redirect
#user ceration form
from django.contrib.auth.forms import UserCreationForm
#flash messages
from django.contrib import messages
#custom forms
from .forms import *
# login requred decorator(used to limit views to logedin people)
from django.contrib.auth.decorators import login_required



def register(request):
    #checks for post request
    if request.method == 'POST':
        #creates form with data from the post request
        form = UserRegesterForm(request.POST)
        #cheks if form is valid
        if form.is_valid():
            #saves the user data
            form.save()
            #extracts clean data from the form using form.cleaned_data
            username = form.cleaned_data.get('username')
            #send a flash message confirming that our data is valid
            messages.success(request, f'Your account has been created you may now login')
            # redirects us back to blog home
            return redirect('login')
    else:
        form = UserRegesterForm()
    return render(request, 'users/regester.html', {'form':form})
    #{'form':form} is the context that passes the form that we want to use

# profile view with login requred decorator
# diffrent with class based views
@login_required
def profile(request):
    if request.method == 'POST':
        #imports our profile forms, and sets usere info to the feilds
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES, 
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            
            p_form.save()
            #send a flash message confirming that our data is valid
            messages.success(request, f'Your account has been Updated')
            # redirects us back to profile becuse of the post, get redierct pattern(reloading the page causes a post request) 
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form':u_form, 
        'p_form' : p_form
    }
    return render(request, 'users/profile.html', context)

"""
types of flash messages for django
messages.debug
mssages.info 
messages.success
messages.warning 
messages.error
"""