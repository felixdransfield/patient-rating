"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import settings
admin.autodiscover()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'symptom_tracker.views.home'),
    url(r'^patient/', include('rating.urls')),
    url(r'^accounts/', include('userprofile.urls')),
    url(r'^chart/', include('charts.urls')),
    url(r'^patient/', include('events.urls')),


    # User auth urls
    url(r'^accounts/login/$', 'symptom_tracker.views.login'),
    url(r'^accounts/auth/$', 'symptom_tracker.views.auth_view'),
    url(r'^accounts/logout/$', 'symptom_tracker.views.logout'),
    url(r'^accounts/loggedin/$', 'symptom_tracker.views.loggedin'),
    url(r'^accounts/invalid/$', 'symptom_tracker.views.invalid_login'),
    url(r'^accounts/register/$', 'symptom_tracker.views.register_user'),
    url(r'^accounts/register_success/$', 'symptom_tracker.views.register_success'),


]


if not settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()