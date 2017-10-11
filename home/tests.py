from __future__ import unicode_literals
from django.test import TestCase
from home.views import get_index
from django.core.urlresolvers import resolve
from accounts.models import User


# Create your tests here.
class HomePageTest(TestCase):
    fixtures = ['subjects', 'user']

    def setUp(self):
        super(HomePageTest, self).setUp()
        self.user = User.objects.create(username='testuser')
        self.user.set_password('logmein')
        self.user.save()
        self.login = self.client.login(username='testuser', password='logmein')
        self.assertEqual(self.login, True)

    def test_home_page_resolves(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, get_index)

    def test_home_page_status_code_is_ok(self):
        home_page = self.client.get('/')
        self.assertEqual(home_page.status_code, 200)

    def test_check_content_is_correct(self):
        home_page = self.client.get('/')
        self.assertTemplateUsed(home_page, 'index.html')
