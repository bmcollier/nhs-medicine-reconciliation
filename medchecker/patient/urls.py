from django.conf.urls import patterns, url

urlpatterns = patterns('patient.views',
    url(r'^$', 'search', name='patient_search'),
    url(r'^add/$', 'add', name='patient_add'),
    url(r'^(?P<patient_id>[0-9]*)/$', 'detail', name='patient_detail'),
    url(r'^(?P<patient_id>[0-9]*)/add_medicine/$', 'add_medicine', name='patient_add_medicine'),
    )