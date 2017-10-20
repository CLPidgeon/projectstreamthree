from django import template
from django.core.urlresolvers import reverse
from django.utils import timezone


register = template.Library()


# Code taken from Code Insitute lesson
@register.simple_tag
def user_vote_button(issue, user):
    """Creates the user voting button for bugs"""
    vote = issue.issue_votes.filter(user_id=user.id).first()
    if not vote:
        if user.is_authenticated():
            link = """
           <a href="%s" class="btn vote-button btn-sm">
             I have this!
           </a>
           </div>""" % reverse('issue_vote', kwargs={'issue_id': issue.id})
            return link
    return ""


# Code edited from Code Institute lesson
@register.simple_tag
def user_feature_vote_button(issue, user):
    """Creates voting button for subscribed users for features"""
    vote = issue.issue_votes.filter(user_id=user.id).first()
    if user.subscription_end > timezone.now():
        if not vote:
            if user.is_authenticated():
                link = """
                <a href="%s" class="btn vote-button btn-sm">
                 I want this!
                </a>
                </div>""" % reverse('issue_vote', kwargs={'issue_id': issue.id})
                return link
    return ""


# Code taken from Code Institute lesson
@register.filter
def total_votes(issue_id):
    """Counting up the votes"""
    count = issue_id.issue_votes.count()
    return count
