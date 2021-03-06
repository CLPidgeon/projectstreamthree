from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, UserManager


# Code edited from Code Institute Lesson
class AccountUserManager(UserManager):
    """Creating the User"""
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('Please enter your email address')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


# Code edited from Code Institute Lesson
class User(AbstractUser):
    """Adds subscription information to User details"""
    stripe_id = models.CharField(max_length=40, default='')
    subscription_end = models.DateTimeField(default=timezone.now)
    objects = AccountUserManager()

    def is_subscribed(self):
        return self.subscription_end > timezone.now()
