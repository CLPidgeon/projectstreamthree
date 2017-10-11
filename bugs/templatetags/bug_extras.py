from django import template
from django.core.urlresolvers import reverse


register = template.Library()


@register.simple_tag
def user_vote_button(bug, user):

    vote = bug.bug_votes.filter(user_id=user.id).first()

    if not vote:
        if user.is_authenticated():
            link = """
           <a href="%s" class="btn vote-button btn-sm">
             I have this!
           </a>
           </div>""" % reverse('bug_vote', kwargs={'bug_id': bug.id})

            return link

    return ""


@register.filter
def total_votes(bug_id):

    count = bug_id.bug_votes.count()

    return count
