from __future__ import unicode_literals
from django.test import TestCase
from .views import get_index, get_fantasy, get_about, get_contact
from django.core.urlresolvers import resolve
from accounts.models import User


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


class FantasyPageTest(TestCase):

    def test_fantasy_page_resolves(self):
        fantasy_page = resolve('/fantasy')
        self.assertEqual(fantasy_page.func, get_fantasy)

    def test_fantasy_page_status_code_is_ok(self):
        fantasy_page = self.client.get('/fantasy')
        self.assertEqual(fantasy_page.status_code, 200)

    def test_fantasy_content_is_correct(self):
        fantasy_page = self.client.get('/fantasy')
        self.assertTemplateUsed(fantasy_page, 'fantasyIH.html')


class ContactPageTest(TestCase):

    def test_contact_page_resolves(self):
        contact_page = resolve('/contact')
        self.assertEqual(contact_page.func, get_contact)

    def test_contact_page_status_code_is_ok(self):
        contact_page = self.client.get('/contact')
        self.assertEqual(contact_page.status_code, 200)

    def test_contact_content_is_correct(self):
        contact_page = self.client.get('/contact')
        self.assertTemplateUsed(contact_page, 'contact.html')


class AboutPageTest(TestCase):

    def test_about_page_resolves(self):
        about_page = resolve('/about')
        self.assertEqual(about_page.func, get_about)

    def test_about_page_status_code_is_ok(self):
        about_page = self.client.get('/about')
        self.assertEqual(about_page.status_code, 200)

    def test_about_content_is_correct(self):
        about_page = self.client.get('/about')
        self.assertTemplateUsed(about_page, 'about.html')
