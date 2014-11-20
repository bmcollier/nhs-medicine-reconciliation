from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^parse_medicine_text/$', 'medicine.ajax.parse_medicine_text', name='ajax_parse_medicine_text'),
    url(r'^suggest_barcode/$', 'medicine.ajax.suggest_barcode', name='ajax_suggest_barcode'),
    url(r'^drop_medicine/$', 'medicine.ajax.drop_medicine', name='ajax_drop_medicine'),
    url(r'^delete_medicine/$', 'medicine.ajax.delete_medicine', name='ajax_delete_medicine')
    )  