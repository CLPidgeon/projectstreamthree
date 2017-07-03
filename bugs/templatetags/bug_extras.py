from django import template
from django.core.urlresolvers import reverse


register = template.Library()


@register.simple_tag
def user_vote_button(bug, user):

    vote = bug.votes

    if not vote:
        if user.is_authenticated():
            link = """
           <a href="%s" class="btn btn-default btn-sm" onclick="vote(Bug)">
             I have this!
           </a>
           </div>""" % reverse('bug_vote', kwargs={'bug_id': bug.id})

            return link

    return ""


@register.filter
def add_vote(bug):

    total = bug.votes.count()
    total += 1

    return total
