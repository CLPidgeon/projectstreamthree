from django import template
from django.core.urlresolvers import reverse
from django.utils import timezone


register = template.Library()


@register.simple_tag
def user_vote_button(feature, user):

    if user.subscription_end > timezone.now():
            link = """
           <a href="%s" class="btn btn-default btn-sm" onclick="vote()">
             I want this!
           </a>
           </div>""" % reverse('feature_vote', kwargs={'feature_id': feature.id})

            return link


    return ""


@register.filter
def vote_total(feature):

    count = feature.votes.count()

    return count