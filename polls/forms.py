from django import forms
from models import Poll, PollSubject


# Code taken from Code Institute lesson
class PollForm(forms.ModelForm):
    question = forms.CharField(label='Poll question:')

    class Meta:
        model = Poll
        fields = ['question']


class PollSubjectForm(forms.ModelForm):
    name = forms.CharField(label='Poll option:', required=True)

    def __init__(self, *args, **kwargs):
        super(PollSubjectForm, self).__init__(*args, **kwargs)
        self.empty_permitted = False

    class Meta:
        model = PollSubject
        fields = ['name']
