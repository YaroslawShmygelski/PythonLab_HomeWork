from django.shortcuts import render
from django.utils import timezone
from django.views.generic import DetailView
from django.views.generic.list import ListView

from .models import Post


# Create your views here.

class HomePageView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/home.html'


class DetailPageView(DetailView):
    model = Post
    context_object_name = 'post'
