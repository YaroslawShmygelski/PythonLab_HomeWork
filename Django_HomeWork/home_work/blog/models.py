from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from .utils import unique_slugify


class User(AbstractUser):
    bio = models.TextField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, null=False, blank=False)


class Post(models.Model):
    title = models.CharField(max_length=20, blank=False, null=False)
    slug = models.SlugField(blank=True)
    content = models.TextField(max_length=100, blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.FileField(upload_to='photos/%Y/%m/%d/',
                             blank=True, null=True, verbose_name="Photo")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.title))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:post-detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ['-created_at']