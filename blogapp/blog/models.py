from django.db import models
from django.conf import settings
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100, help_text='Enter post title')
    author = models.ForeignKey('BlogAuthor', on_delete=models.SET_NULL, null=True)
    post_date = models.DateField(default=date.today)
    description = models.CharField(max_length=1000, help_text="Enter the content of the blog")
    
    class meta:
        ordering=['post_date']
    
    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return f"{self.title}"
    
class BlogAuthor(models.Model):
    name = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.CharField(max_length=1000, help_text="Enter the biograpy of the author")
    
    def __str__(self):
        return f"{self.name}"
    
class BlogComment(models.Model):
    description = models.TextField(max_length=1000, help_text="Enter the comment")
    post_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    
    def __str__(self):
        len_title=75
        if len(self.description) > len_title:
            titleString = self.description[:len_title]
        else:
            titleString = self.description
        return titleString