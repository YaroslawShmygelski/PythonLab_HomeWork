from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('post-detail/<slug:slug>/', views.ProductDetailView.as_view(), name='post-detail'),
    path('create-post/', views.CreatePostView.as_view(), name='create-post'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.UserCreationView.as_view(), name='register')
]
