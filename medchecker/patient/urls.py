from django.conf.urls import patterns, url

urlpatterns = patterns('patient.views',
    url(r'^$', 'search', name='patient_search'),
    url(r'^add/$', 'add', name='patient_add'),
    url(r'^(?P<patient_id>[0-9]*)/$', 'detail', name='patient_detail'),
    url(r'^(?P<patient_id>[0-9]*)/add_medication/$', 'add_medicine', name='patient_add_medicine'),
    url(r'^(?P<patient_id>[0-9]*)/edit_medication/$', 'edit_medicine', name='patient_edit_medicine'),
    url(r'^(?P<patient_id>[0-9]*)/edit_medication/(?P<medicine_id>[0-9]*)/$', 'edit_medicine', name='patient_edit_medicine'),
    url(r'^(?P<patient_id>[0-9]*)/reconcile_medications/$', 'reconcile_medicines', name='patient_reconcile_medicine'),
    url(r'^(?P<patient_id>[0-9]*)/verify_medications/$', 'verify_medicine', name='patient_verify_medicine'),
    url(r'^(?P<patient_id>[0-9]*)/discharge/$', 'discharge', name='patient_discharge'),
    url(r'^(?P<patient_id>[0-9]*)/scan_medication/$', 'scan_medicine', name='patient_scan_medicine'),
    )