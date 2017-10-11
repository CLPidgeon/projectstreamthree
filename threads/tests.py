from __future__ import unicode_literals
from django.test import TestCase
from django.shortcuts import render_to_response
from threads.models import Subject
from threads.views import forum, threads, new_thread, thread, new_post, edit_post, delete_post, thread_vote
from django.core.urlresolvers import resolve


class ForumPageTest(TestCase):
    def test_forum_page_resolves(self):
        main_forum = resolve('/forum/')
        self.assertEqual(main_forum.func, forum)

    def test_check_content_is_correct(self):
        subject_page = self.client.get('/forum/')
        self.assertTemplateUsed(subject_page, 'forum/forum.html')
        subject_page_template_output = render_to_response('forum/forum.html',
                                                          {'subjects': Subject.objects.all()}).content
        self.assertEqual(subject_page.content, subject_page_template_output)

    def test_threads_resolve(self):
        threads_list = resolve('/threads/1/')
        self.assertEqual(threads_list.func, threads)

    def test_new_thread_resolves(self):
        new_threads = resolve('/new_thread/1/')
        self.assertEqual(new_threads.func, new_thread)

    def test_thread_page_resolves(self):
        thread_list = resolve('/thread/1/')
        self.assertEqual(thread_list.func, thread)

    def test_new_post_resolves(self):
        new_posts = resolve('/post/new/1/')
        self.assertEqual(new_posts.func, new_post)

    def test_edit_post_resolves(self):
        edit_posts = resolve('/post/edit/1/2/')
        self.assertEqual(edit_posts.func, edit_post)

    def test_delete_post_resolves(self):
        delete_posts = resolve('/post/delete/1/2/')
        self.assertEqual(delete_posts.func, delete_post)

    def test_voting_resolves(self):
        voting = resolve('/thread/vote/1/2/')
        self.assertEqual(voting.func, thread_vote)
