import arrow
from django import template
from django.core.urlresolvers import reverse

register = template.Library()


# Code taken from Code Institute Lesson
@register.filter
def get_total_subject_posts(subject):
    """Gets the total number of posts on a subject"""
    total_posts = 0
    for thread in subject.threads.all():
        total_posts += thread.posts.count()
    return total_posts


@register.filter
def get_total_thread_posts(thread):
    """Gets the total number of posts on a thread"""
    total_posts = thread.posts.count()
    return total_posts


@register.filter
def started_time(created_at):
    return arrow.get(created_at).humanize()


@register.simple_tag
def last_posted_user_name(thread):
    posts = thread.posts.all().order_by('-created_at')
    return posts[posts.count()-1].user.username


@register.simple_tag
def user_vote_button(thread, subject, user):
    vote = thread.poll.votes.filter(user_id=user.id).first()
    if not vote:
        if user.is_authenticated():
            link = """
           <div class="col-md-3 btn-vote">
           <a href="%s" class="btn vote-button btn-sm">
             Add my vote!
           </a>
           </div>""" % reverse('cast_vote', kwargs={'thread_id': thread.id, 'subject_id': subject.id})
            return link
    return ""


@register.filter
def vote_percentage(subject):
    count = subject.votes.count()
    if count == 0:
        return 0
    total_votes = subject.poll.votes.count()
    return (100/total_votes) * count
