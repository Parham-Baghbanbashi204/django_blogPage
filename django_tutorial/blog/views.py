from django.shortcuts import render
from .models import Post
from django.views.generic import (ListView, 
DetailView, 
CreateView,
UpdateView,
DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
"""
def home(request):
    return HttpResponse('<h1>Blog Home</h1>')  # displays Blog home can be used to display HTML homepage
    # function must be maped to a url in urls.py in the app dir
    # ise HttpResponse to desplay HTML webpages
"""


# Function based view
# homepage using templates
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# class based views
# these class based views allow us to use djangos defult views and modify them
class PostListView(ListView):
    # we get these atributes form the ListViews MultipleObjectTemplateResponseMixin
    # we can cut down on these atributes if we use the proper django conventions
    model = Post
    # template it uses
    template_name = 'blog/home.html' # django template nameing convention: <app>/<model>_<viewtype>.html
    # contex
    context_object_name = 'posts'
    # to allow us to display the newest post first we need to change the order of our qurery
    # this attribute allows the backent to determine which atribute to order the posts by
    ordering = ['-date_posted']# the minus sign orders the dates by newest to oldest


# keeping to the conventions
# looking at a single post
class PostDetailView(DetailView):
    model = Post
    #looks for template blog/post_detail.html

# creating posts
# createview is a view with a form
# class based views allow django to handle stuff in the background
# mixens are added to the far left
# MAKING IS SO THAT ONLY USERS CAN ACCSES THIS VIEW
# MIXIN --> class that adds extra functionalty to the view
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # we need to add feilds 
    fields = ['title', 'content']
    # for CreateView the convention is <model>_form.html

    # assigns an author to the PostCreateView --> assigns author to new post
    # reminder this class creates posts
    # helps us avoid integraty errors
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # if we want to go to the homepage insted of deataled view set sucsess_url to homepage
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    # for UpdateView the convention is <model>_form.html
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # checks if the user that wants to update the form is the user that created it
    def test_func(self):
        post = self.get_object()
        if self.request.user ==  post.author:
            return True
        return False

# delete view
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # template convention is <model>_confirm_delete.html
    # checks if the user that wants to delete the form is the user that created it
    def test_func(self):
        post = self.get_object()
        if self.request.user ==  post.author:
            return True
        return False
    success_url = '/'


'''
def about(request):
    return HttpResponse('<h1>Blog About</h1>')
'''

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})