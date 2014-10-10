from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/$', 'medchecker.views.do_login', name='login'),
    url(r'^home/$', TemplateView.as_view(template_name='base.html'), name="home"),
    url(r'^patient_history_summary/$', TemplateView.as_view(template_name='patient_history_summary.html'), name="patient_history_summary"),
    url(r'^medicine_reconciliation/$', TemplateView.as_view(template_name='medicine_reconciliation.html'), name="medicine_reconciliation"), 
    )  
# Uncomment the next line to serve media files in dev.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
