# -*- coding: utf-8 -*-
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


class Feature(models.Model):

    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=255, null=False)
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, default='Todo')
    updated = models.DateTimeField(default=timezone.now)
    votes = models.IntegerField(default=0)

    def __unicode__(self):

        return self.title


class Comments(models.Model):

    feature = models.ForeignKey(Feature, related_name='comments')
    comments = models.CharField(max_length=255, default='')
    created_at = models.DateTimeField(default=timezone.now)


class Vote( models.Model):

    feature = models.ForeignKey(Feature, related_name='feature_votes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='feature_votes')
