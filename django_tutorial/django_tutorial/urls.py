"""django_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#user regestration views
from users import views as user_views
# django defult views
from django.contrib.auth import views as auth_views

#allows us to accses static media
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # one per app
    # when people navigate to the blog url it then sends them to the blog app urls.py

    #user regestration
    path('regester/', user_views.register, name="register"),

    #login path
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    #login and logout are class based views --> these django defult views will handle the form portions and backend but they 
    #will not touch the templates 
    # to give the login and logout views the templates that we want to use we can pass the template.html through the as_view() function

    #link to out profile page
    path('profile/', user_views.profile, name='profile')

]

#adds our static images urls to urls
# only adds media and static urls if in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)