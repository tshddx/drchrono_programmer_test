from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'drchrono_programmer_test.views.home', name='home'),
    # url(r'^drchrono_programmer_test/', include('drchrono_programmer_test.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
                       
    # The following line serves the css files:
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': r'site_media'}),
                       
    (r'', include('uiforms.urls')),
)
