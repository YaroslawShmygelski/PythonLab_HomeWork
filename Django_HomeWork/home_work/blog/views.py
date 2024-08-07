from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, CreateView, UpdateView
from django.views.generic.list import ListView

from .forms import PostForm, UserLoginForm, UserRegisterForm
from .models import Post


# Create your views here.

class HomePageView(ListView):
    paginate_by = 4
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


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'blog/post-create-form.html'
    fields = ['title', 'content', 'photo']
    success_url = reverse_lazy('blog:home')


class UserLoginView(LoginView):
    template_name = 'blog/user-login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy("blog:home")


def logout_view(request):
    logout(request)
    return redirect("blog:home")


class UserCreationView(CreateView):
    form_class = UserRegisterForm
    template_name = 'blog/user-registration.html'
    success_url = reverse_lazy('blog:login')
