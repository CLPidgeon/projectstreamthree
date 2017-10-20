from __future__ import unicode_literals
from django.test import TestCase
from .views import fantasy_eihl
from django.core.urlresolvers import resolve


class FantasyStandingsTest(TestCase):

    def test_fantasy_standings_page_resolves(self):
        fantasy_standings_page = resolve('/EIHL/')
        self.assertEqual(fantasy_standings_page.func, fantasy_eihl)

    def test_fantasy_page_status_code_is_ok(self):
        fantasy_standings_page = self.client.get('/EIHL/')
        self.assertEqual(fantasy_standings_page.status_code, 200)

    def test_fantasy_content_is_correct(self):
        fantasy_standings_page = self.client.get('/EIHL/')
        self.assertTemplateUsed(fantasy_standings_page, 'leaguepages/eihl.html')