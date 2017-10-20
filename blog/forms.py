from django import forms
from .models import Post


# Code taken from Code Institute lesson
class BlogPostForm(forms.ModelForm):
    "New blog form"
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'tag')
