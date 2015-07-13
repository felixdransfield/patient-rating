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



urlpatterns = [
    #Shows all patients
    url(r'^all/$', 'rating.views.patients'),

    #Shows individual patient based on patient_id variable
    url(r'^get/(?P<patient_id>\d+)/$', 'rating.views.patient'),

    #create patient form
    url(r'^create/$', 'rating.views.create'),

    #depreceated
    url(r'^update/(?P<patient_id>\d+)/$', 'rating.views.update_patient'),

    #create new panss rating
    url(r'^panss/new/(?P<patient_id>\d+)/$', 'rating.views.panssForm'),

    #show previous panss ratings
    url(r'^panss/(?P<patient_id>\d+)/$', 'rating.views.panss'),

    #create new HCR20 rating
    url(r'^HCR20/new/(?P<patient_id>\d+)/$', 'rating.views.hcr20Form'),

    #show previous HCR20 ratings
    url(r'^HCR20/(?P<patient_id>\d+)/$', 'rating.views.hcr20'),





]
