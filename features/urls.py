from django.conf.urls import url
from features.views import FeatureView
import views


urlpatterns = [

    url(r'^$', FeatureView.as_view()),
    url(r'(?P<pk>[0-9]+)/$/', FeatureView.as_view()),

    #bugs
    url(r'tracker', views.feature_tracker, name='feature_tracker'),
    url(r'new', views.new_feature, name='new_feature'),
]
