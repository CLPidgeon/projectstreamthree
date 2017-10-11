from django import template
from django.core.urlresolvers import reverse


register = template.Library()


@register.simple_tag
def user_vote_button(issue, user):

    vote = issue.issue_votes.filter(user_id=user.id).first()
    if not vote:
        if user.is_authenticated():
            link = """
           <a href="%s" class="btn vote-button btn-sm">
             Upvote!
           </a>
           </div>""" % reverse('issue_vote', kwargs={'issue_id': issue.id})
            return link
    return ""


@register.filter
def total_votes(issue_id):

    count = issue_id.issue_votes.count()
    return count