from django.conf.urls import patterns, url

urlpatterns = patterns('patient.views',
    url(r'^search/$', 'search', name='patient_search'),
    url(r'^add/$', 'add', name='patient_add'),
    url(r'^(?P<patient_id>[0-9]*)/$', 'detail', name='patient_detail'),
    )