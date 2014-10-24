from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

# Regular URLs
urlpatterns = patterns('',
    url(r'^', include('core.urls')),
    url(r'^medicine/', include('medicine.urls')),
    url(r'^patient/', include('patient.urls')),

    url(r'^$', 'core.views.home', name='core_home'),
    )

# AJAX URLs
urlpatterns += patterns('',
    url(r'^' + settings.AJAX_URL + 'medicine/', include('medicine.urlsajax')),
    url(r'^' + settings.AJAX_URL + 'patient/', include('patient.urlsajax')),
)



urlpatterns += patterns('',
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )