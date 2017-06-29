from django import template
from django.core.urlresolvers import reverse


register = template.Library()


@register.simple_tag
def user_vote_button(bug, user):

    vote = bug.votes

    if not vote:
        if user.is_authenticated():
            link = """
           <a href="%s" class="btn btn-default btn-sm" onclick="vote()">
             I have this!
           </a>
           </div>""" % reverse('bug_vote', kwargs={'bug_id': bug.id})

            return link

    return ""


@register.filter
def vote_total(bug):

    count = bug.votes.count()
    if count == 0:
        return 0

    total_votes = bug.votes.count()

    return total_votes
