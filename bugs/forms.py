from django import forms
from .models import Bug, Comments


class BugForm(forms.ModelForm):

    class Meta:

        model = Bug
        fields = ('title', 'description')


class CommentForm(forms.ModelForm):

    class Meta:

        model = Comments
        fields = ['comments']
