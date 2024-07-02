from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    bio = models.TextField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, null=False, blank=False)
