from django.conf.urls import url
from features.views import FeatureView
import views


urlpatterns = [

    url(r'^admin/$', FeatureView.as_view()),
    url(r'^admin/(?P<pk>[0-9]+)/$', FeatureView.as_view()),

    # Features
    url(r'tracker/$', views.feature_tracker, name='feature_tracker'),
    url(r'new', views.new_feature, name='new_feature'),
    url(r'vote/(?P<feature_id>[0-9]+)/$', views.feature_tracker, name='feature_vote'),
    url(r'(?P<id>[0-9]+)/$', views.feature_comment),
]