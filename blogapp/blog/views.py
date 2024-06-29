from django.shortcuts import render
from .models import Blog, BlogAuthor
from django.views.generic import ListView

# Create your views here.
def index(request):
    num_blogs = Blog.objects.all().count()
    num_blogAuthors = BlogAuthor.objects.all().count()
    print(num_blogs)
    context = {
        'num_blogs': num_blogs,
        'num_blogAuthors': num_blogAuthors
    }
    return render(request, 'index.html', context=context)

class BlogListView(ListView):
    model = Blog

class BlogAuthorListView(ListView):
    model = BlogAuthor
