from django.conf.urls import url
from bugs.views import BugView
import views


urlpatterns = [

    url(r'^$', BugView.as_view()),
    url(r'(?P<pk>[0-9]+)/$', BugView.as_view()),

    #bugs
    url(r'tracker', views.bug_tracker, name='bug_tracker'),
    url(r'new', views.new_bug, name='new_bug'),
    url(r'comment', views.bug, name='bug'),
]
