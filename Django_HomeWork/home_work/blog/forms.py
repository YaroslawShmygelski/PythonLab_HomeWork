from django.forms import ModelForm, TextInput, Textarea, FileInput

from .models import Post


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
