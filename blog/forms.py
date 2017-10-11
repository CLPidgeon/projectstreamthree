from django import forms
from .models import Post


class BlogPostForm(forms.ModelForm):
    "New blog form"
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'tag')
