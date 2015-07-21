__author__ = 'felixdransfield'
from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^profile/edit/(?P<user_id>\d+)/$', 'userprofile.views.edit_profile'),
    url(r'^profile/(?P<user_id>\d+)/$', 'userprofile.views.user_profile'),
]