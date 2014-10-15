from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^add/$', TemplateView.as_view(template_name='medicine_add.html'), name='medicine_add'),
    )  