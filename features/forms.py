from django import forms
from .models import Feature, Comments


class FeatureForm(forms.ModelForm):

    class Meta:

        model = Feature
        fields = ('title', 'description')


class CommentForm(forms.ModelForm):

    class Meta:

        model = Comments
        fields = ['comments']
