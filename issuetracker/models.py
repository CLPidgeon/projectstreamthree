from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.conf import settings


# Create your models here.
STATUS_CHOICES = (
    ('Todo', 'Todo'),
    ('Doing', 'Doing'),
    ('Done', 'Done')
)

TYPE = (
    ('Bug', 'Bug'),
    ('Feature', 'Feature')
)


class Issue(models.Model):

    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=255, null=False)
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, default='Todo')
    type = models.CharField(max_length=7, choices=TYPE, default='Bug')
    updated = models.DateTimeField(default=timezone.now)

    def __unicode__(self):

        return self.title

    def get_bugs(self):
        return self.objects.filter(type='Bug')

    def get_features(self):
        return self.objects.filter(type='Feature')


class Comments(models.Model):

    issue = models.ForeignKey(Issue, related_name='comments')
    comments = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)


class Vote(models.Model):

    Issue = models.ForeignKey(Issue, related_name='issue_votes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='issue_votes')