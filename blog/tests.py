from __future__ import unicode_literals
from django.test import TestCase
from blog.views import post_list, post_detail, edit_post, new_post
from django.core.urlresolvers import resolve


# Create your tests here.
class BlogPageTest(TestCase):
    def test_blog_list_resolves(self):
        blog_list = resolve('/blog/')
        self.assertEqual(blog_list.func, post_list)

    def test_blog_list_status_code(self):
        blog_list = self.client.get('/blog/')
        self.assertEqual(blog_list.status_code, 200)

    def test_blog_list_template_correct(self):
        blog_list = self.client.get('/blog/')
        self.assertTemplateUsed(blog_list, 'blogposts.html')

    def test_blog_detail_resolves(self):
        blog_detail = resolve('/blog/1/')
        self.assertEqual(blog_detail.func, post_detail)

    def test_new_blog_resolves(self):
        new_blog = resolve('/post/new/')
        self.assertEqual(new_blog.func, new_post)

    def test_new_blog_status_code(self):
        new_blog = self.client.get('/post/new/')
        self.assertEqual(new_blog.status_code, 200)

    def test_new_blog_template_correct(self):
        new_blog = self.client.get('/post/new/')
        self.assertTemplateUsed(new_blog, 'blogpostform.html')

    def test_edit_blog_resolves(self):
        edit_blog = resolve('/blog/1/edit')
        self.assertEqual(edit_blog.func, edit_post)
