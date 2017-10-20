from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from threads.models import Thread


# Code taken from Code Institute lesson
class Poll(models.Model):
    """Setting up Poll model and linking it to the thread"""
    question = models.TextField()
    thread = models.OneToOneField(Thread, null=True)

    def __unicode__(self):
        return self.question


# Code taken from Code Insitute lesson
class PollSubject(models.Model):
    """Setting up Poll subject and linking it to the Poll"""
    name = models.CharField(max_length=255)
    poll = models.ForeignKey(Poll, related_name='subjects')

    def __unicode__(self):
        return self.name


# Code taken from Code Institute lesson
class Vote(models.Model):
    """Setting up the voting and linking it to the Poll, Subject and User voting"""
    poll = models.ForeignKey(Poll, related_name='votes')
    subject = models.ForeignKey(PollSubject, related_name='votes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='votes')
