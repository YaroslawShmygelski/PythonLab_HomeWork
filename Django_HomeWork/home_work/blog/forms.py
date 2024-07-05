from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm, TextInput, Textarea, FileInput, EmailInput, PasswordInput

from .models import Post, User


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'photo']
        widgets = {
            'title': TextInput(
                attrs={'placeholder': 'Input Title',
                       'class': 'title-input'
                       }
            ),
            'content': Textarea(
                attrs={'placeholder': 'Place your content here',
                       'class': 'content-input'
                       }
            ),
            'photo': FileInput(
                attrs={'placeholder': 'Input Title',
                       'class': 'file-chooser-input'
                       }
            )
        }


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
        widgets = {
            "username": EmailInput(
                attrs={'placeholder': 'Input Title',
                       'class': 'title-input'
                       }
            ),
              "password": PasswordInput(
                attrs={'placeholder': 'Input password',
                       }
            )
        }


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'bio', 'email']
        widgets = {
            "username": TextInput(
                attrs={'placeholder': 'Input username',
                       }
            ),
            "password": PasswordInput(
                attrs={'placeholder': 'Input password',
                       }
            ),
            "password2": PasswordInput(
                attrs={'placeholder': 'Repeat password'}
            ),
            'bio': Textarea(
                attrs={'placeholder': 'Input text'}
            ),
            'email': EmailInput(
                attrs={'placeholder': 'Input email'}
            )
        }
