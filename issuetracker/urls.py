from django.conf.urls import url
from .views import IssueView
import views


urlpatterns = [
    # Issue admin
    url(r'^admin/$', IssueView.as_view()),
    url(r'admin/(?P<pk>[0-9]+)/$', IssueView.as_view()),

    # Issue Tracker
    url(r'tracker/$', views.issue_tracker, name='issue_tracker'),
    url(r'new', views.new_issue, name='new_issue'),
    url(r'vote/(?P<issue_id>[0-9]+)/$', views.issue_vote, name='issue_vote'),
    url(r'(?P<issue_id>[0-9]+)/$', views.issue_detail, name='issue'),
    url(r'(?P<issue_id>[0-9]+)/comment/$', views.issue_comment, name='issue_comment'),
]
