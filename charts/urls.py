__author__ = 'felixdransfield'

"""symptom_tracker URL Configuration

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
#from api import PatientResource

#patient_resource = PatientResource()



#Loads Charts for both PANSS and HCR20 - split into their sub scales
urlpatterns = [
    url(r'^Panss/Positive/(?P<patient_id>\d+)/$', 'charts.views.Pchart'),
    url(r'^Panss/Negative/(?P<patient_id>\d+)/$', 'charts.views.Nchart'),
    url(r'^Panss/General/(?P<patient_id>\d+)/$', 'charts.views.Gchart'),
    url(r'^Panss/Additional/(?P<patient_id>\d+)/$', 'charts.views.Schart'),
    url(r'^HCR20/Historical/(?P<patient_id>\d+)/$', 'charts.views.Hchart'),
    url(r'^HCR20/Clinical/(?P<patient_id>\d+)/$', 'charts.views.Cchart'),
    url(r'^HCR20/Risk/(?P<patient_id>\d+)/$', 'charts.views.Rchart'),




]






