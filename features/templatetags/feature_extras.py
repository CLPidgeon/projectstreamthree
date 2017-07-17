from django import template
from django.core.urlresolvers import reverse
from django.utils import timezone


register = template.Library()


@register.simple_tag
def user_vote_button(feature, user):

    vote = feature.feature_votes.filter(user_id=user.id).first()

    if not vote:

        if user.subscription_end > timezone.now():
            link = """
           <a href="%s" class="btn vote-button btn-sm" onclick="vote()">
             I want this!
           </a>
           </div>""" % reverse('feature_vote', kwargs={'feature_id': feature.id})

            return link


    return ""


@register.filter
def total_votes(feature_id):

    count = feature_id.feature_votes.count()

    return count