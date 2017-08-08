# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from bugs.views import bug_tracker, new_bug, bug, bug_comment, bug_vote
from django.core.urlresolvers import resolve


# Create your tests here.
class BugPageTest(TestCase):

    def test_bug_tracker_resolves(self):

        bugs_tracker = resolve('/bugs/tracker/')
        self.assertEqual(bugs_tracker.func, bug_tracker)

    def test_new_bug_resolves(self):

        new_bug_form = resolve('/bugs/new')
        self.assertEqual(new_bug_form.func, new_bug)

    def test_bug_resolves(self):

        bug_details = resolve('/bugs/1/')
        self.assertEqual(bug_details.func, bug)

    def test_bug_comments_resolves(self):

        bug_comments = resolve('/bugs/1/comment/')
        self.assertEqual(bug_comments.func, bug_comment)

    def test_bug_voting_resolves(self):

        bug_voting = resolve('/bugs/vote/1/')
        self.assertEqual(bug_voting.func, bug_vote)
