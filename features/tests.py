# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from features.views import feature_tracker, new_feature, feature, feature_comment, feature_vote
from django.core.urlresolvers import resolve


# Create your tests here.
class FeaturePageTest(TestCase):

    def test_feature_tracker_resolves(self):

        features_tracker = resolve('/features/tracker/')
        self.assertEqual(features_tracker.func, feature_tracker)

    def test_new_feature_resolves(self):

        new_feature_form = resolve('/features/new')
        self.assertEqual(new_feature_form.func, new_feature)

    def test_feautre_resolves(self):

        feature_details = resolve('/features/1/')
        self.assertEqual(feature_details.func, feature)

    def test_feature_comments_resolves(self):

        feature_comments = resolve('/features/1/comment/')
        self.assertEqual(feature_comments.func, feature_comment)

    def test_feature_voting_resolves(self):

        feature_voting = resolve('/features/vote/1/')
        self.assertEqual(feature_voting.func, feature_vote)
