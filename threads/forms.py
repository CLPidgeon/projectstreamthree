from django import forms
from .models import Thread, Post


# Code taken from Code Institute Lesson
class ThreadForm(forms.ModelForm):
    "Thread form with the optional poll form"
    name = forms.CharField(label="Thread name")
    is_a_poll = forms.BooleanField(label="Include a poll?", required=False)

    class Meta:
        model = Thread
        fields = ['name']


class PostForm(forms.ModelForm):
    "Post form to add to a thread"
    class Meta:
        model = Post
        fields = ['comment']
