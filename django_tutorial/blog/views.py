from django.shortcuts import render
from .models import Post

# Create your views here.
"""
def home(request):
    return HttpResponse('<h1>Blog Home</h1>')  # displays Blog home can be used to display HTML homepage
    # function must be maped to a url in urls.py in the app dir
    # ise HttpResponse to desplay HTML webpages
"""


# homepage using templates
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


"""
def about(request):
    return HttpResponse('<h1>Blog About</h1>')
"""


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
