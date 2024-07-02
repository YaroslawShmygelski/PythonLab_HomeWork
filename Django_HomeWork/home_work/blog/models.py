from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    bio = models.TextField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, null=False, blank=False)


class Post(models.Model):
    title = models.CharField(max_length=20, blank=False, null=False)
    content = models.TextField(max_length=100, blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.FileField(upload_to='photos/%Y/%m/%d/',
                             blank=True, null=True, verbose_name="Photo")