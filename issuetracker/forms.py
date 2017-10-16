from django import forms
from .models import Issue, Comments


class IssueForm(forms.ModelForm):

    class Meta:
        model = Issue
        fields = ('title', 'description', 'type')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['comments']
