from django import forms
from models import Poll, PollSubject


# Code taken from Code Institute lesson
class PollForm(forms.ModelForm):
    """Poll form question"""
    question = forms.CharField(label='Poll question:', required=False)

    class Meta:
        model = Poll
        fields = ['question']


class PollSubjectForm(forms.ModelForm):
    """Poll options required for the Poll question"""
    name = forms.CharField(label='Poll option:', required=True)

    def __init__(self, *args, **kwargs):
        super(PollSubjectForm, self).__init__(*args, **kwargs)
        self.empty_permitted = False

    class Meta:
        model = PollSubject
        fields = ['name']
