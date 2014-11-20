from django.conf.urls import patterns, url

urlpatterns = patterns('patient.views',
    url(r'^$', 'search', name='patient_search'),
    url(r'^add/$', 'add', name='patient_add'),
    url(r'^(?P<patient_id>[0-9]*)/$', 'detail', name='patient_detail'),
    url(r'^(?P<patient_id>[0-9]*)/scan_medication/$', 'scan_medicine', name='patient_scan_medicine'),
    url(r'^(?P<patient_id>[0-9]*)/add_medication/$', 'add_medicine', name='patient_add_medicine'),
    url(r'^(?P<patient_id>[0-9]*)/add_medication_gp/$', 'add_medicine_gp', name='patient_add_medicine_gp'),
    url(r'^(?P<patient_id>[0-9]*)/add_medication_last/$', 'add_medicine_last', name='patient_add_medicine_last'),
    url(r'^(?P<patient_id>[0-9]*)/edit_medication/$', 'edit_medicine', name='patient_edit_medicine'),
    url(r'^(?P<patient_id>[0-9]*)/edit_medication/(?P<medication_id>[0-9]*)/$', 'edit_medicine', name='patient_edit_medicine'),
    url(r'^(?P<patient_id>[0-9]*)/reconcile_medications/$', 'reconcile_medicines', name='patient_reconcile_medicine'),
    url(r'^(?P<patient_id>[0-9]*)/reconcile_discharge/$', 'reconcile_discharge', name='patient_reconcile_discharge'),
    url(r'^(?P<patient_id>[0-9]*)/verify_medications/$', 'verify_medicine', name='patient_verify_medicine'),
    url(r'^(?P<patient_id>[0-9]*)/discharge/$', 'discharge', name='patient_discharge'),
    )