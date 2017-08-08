# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from magazines.views import all_magazines
from django.core.urlresolvers import resolve


# Create your tests here.
class SubscriptionPageTest(TestCase):

    def test_subscription_page_resolves(self):

        subscribe = resolve('/subscribe/')
        self.assertEqual(subscribe.func, all_magazines)
