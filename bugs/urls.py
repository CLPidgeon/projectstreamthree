from django.conf.urls import url
from bugs.views import BugView
import views


urlpatterns = [

    url(r'^admin/$', BugView.as_view()),
    url(r'admin/(?P<pk>[0-9]+)/$', BugView.as_view()),

    #bugs
    url(r'tracker/$', views.bug_tracker, name='bug_tracker'),
    url(r'new', views.new_bug, name='new_bug'),
    url(r'vote/(?P<bug_id>[0-9]+)/$', views.bug_vote, name='bug_vote'),
    url(r'tracker/(?P<id>\d+)/$', views.bug_comment),
]
