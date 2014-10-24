from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('core.views',
    url(r'^login/$', 'do_login', name='login'),
    url(r'^unlock/(?P<nfc_token>[a-z0-9\-]*)/$', 'do_unlock', name='unlock'),
    url(r'^logout/$', 'do_logout', name='logout'),
    url(r'^dashboard/$', 'dashboard', name='core_dashboard'),
    url(r'^user_settings/$', 'user_settings', name='core_user_settings'),
    url(r'^$', 'home', name='core_home'),
    )