from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^parse_medicine_text/$', 'medicine.ajax.parse_medicine_text', name='ajax_parse_medicine_text'),
    )  