from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('post-detail/<slug:slug>/', views.ProductDetailView.as_view(), name='post-detail')
]
