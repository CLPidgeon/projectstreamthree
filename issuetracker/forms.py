from django import forms
from .models import Issue, Comments


class IssueForm(forms.ModelForm):
    "Issue form, uses type to differentiate between bugs and issues"
    class Meta:
        model = Issue
        fields = ('title', 'description', 'type')


class CommentForm(forms.ModelForm):
    "Comment form for an issue"
    class Meta:
        model = Comments
        fields = ['comments']
