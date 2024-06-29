from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('bloggers/', views.BlogAuthorListView.as_view(), name='bloggers'),
]