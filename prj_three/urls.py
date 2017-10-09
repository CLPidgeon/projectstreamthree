"""prj_three URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from settings.dev import MEDIA_ROOT
from home import views
from accounts import views as accounts_views
from threads import views as forum_views
from progress import views as progress_views
from leagues import views as league_views
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.get_index, name='index'),

    # Charts
    url(r'^progress/feature', progress_views.featuredata),
    url(r'^progress/bug', progress_views.bugdata),
    url(r'^features/progress', progress_views.features_charts),
    url(r'^bugs/progress', progress_views.bugs_charts),

    # Flatpages
    url(r'^pages/', include('django.contrib.flatpages.urls')),

    # Fantasy Ice Hockey
    url(r'^fantasy', views.fantasy, name='fantasy'),

    # Blog
    url(r'', include('blog.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    # Forum
    url(r'^forum/$', forum_views.forum),
    url(r'^threads/(?P<subject_id>\d+)/$', forum_views.threads, name='threads'),
    url(r'^new_thread/(?P<subject_id>\d+)/$', forum_views.new_thread, name='new_thread'),
    url(r'^thread/(?P<thread_id>\d+)/$', forum_views.thread, name='thread'),
    url(r'^post/new/(?P<thread_id>\d+)/$', forum_views.new_post, name='new_post'),
    url(r'^post/edit/(?P<thread_id>\d+)/(?P<post_id>\d+)/$', forum_views.edit_post, name='edit_post'),
    url(r'^post/delete/(?P<thread_id>\d+)/(?P<post_id>\d+)/$', forum_views.delete_post, name='delete_post'),
    url(r'^thread/vote/(?P<thread_id>\d+)/(?P<subject_id>\d+)/$', forum_views.thread_vote, name='cast_vote'),

    # Accounts
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),

    # Stripe
    url(r'subscribe', accounts_views.subscribe, name='subscribe'),
    url(r'^cancel_subscription/$', accounts_views.cancel_subscription, name='cancel_subscription'),
    url(r'^subscriptions_webhook/$', accounts_views.subscriptions_webhook, name='subscriptions_webhook'),

    # Issue Tracker
    url(r'bugs/', include('bugs.urls')),
    url(r'features/', include('features.urls')),

    # League Pages
    url(r'^EIHL/$', league_views.eihl, name='eihl'),
    url(r'^GB/$', league_views.GB, name="GB"),

]

if settings.DEBUG:

    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

