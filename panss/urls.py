from django.conf.urls import include, url

urlpatterns = [
#show previous panss ratings
    url(r'^(?P<patient_id>\d+)/$', 'panss.views.panss'),
    url(r'^(?P<patient_id>\d+)/(?P<panss_id>\d+)/$', 'charts.views.PanssItemChart'),




#create new panss rating
    url(r'^new/(?P<patient_id>\d+)/$', 'panss.views.panssForm'),
    url(r'^admission/(?P<patient_id>\d+)/$', 'panss.views.panssFormFull'),
    url(r'^full/(?P<patient_id>\d+)/$', 'panss.views.panssFormFull'),
    url(r'^rating-targets/(?P<patient_id>\d+)/(?P<fullpanss_id>\d+)$', 'panss.views.panssTargets'),



#trying to paginate forms
   # url(r'^panss/new/(?P<patient_id>\d+)/$', PANSSWizard.as_view([PANSSPositiveForm, PANSSNegativeForm, PANSSGeneralForm])),

]