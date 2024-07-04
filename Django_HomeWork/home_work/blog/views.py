from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import DetailView, CreateView, FormView
from django.views.generic.list import ListView

from .forms import PostForm
from .models import Post


# Create your views here.

class HomePageView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/home.html'


class ProductDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = "blog/post-detail.html"


class CreatePostView(FormView):
    template_name = 'blog/post-create-form.html'
    form_class = PostForm
    success_url = reverse_lazy('blog:home')

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        form.save()
        return super().form_valid(form)
