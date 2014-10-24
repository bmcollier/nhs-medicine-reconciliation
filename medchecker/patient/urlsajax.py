from django.conf.urls import patterns, url

urlpatterns = patterns('patient.ajax',
    url(r'^(?P<patient_id>[0-9]*)/verify_medicine/$', 'verify_medicine', name='ajax_patient_verify_medicine'),
    )