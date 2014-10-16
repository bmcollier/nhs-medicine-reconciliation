from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('core.views',
    url(r'^login/$', 'do_login', name='login'),
    url(r'^logout/$', 'do_logout', name='logout'),
    url(r'^dashboard/$', 'dashboard', name='core_dashboard'),
    url(r'^$', 'home', name='core_home'),
    )