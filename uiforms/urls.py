from django.conf.urls.defaults import *
from uiforms.views import *

urlpatterns = patterns('uiforms.views',
                       url(r'^register$', 'user_register', name='user_register'),
                       url(r'^login$', 'user_login', name='user_login'),
                       url(r'^logoff$', 'user_logoff', name='user_logoff'),
                       url(r'^dashboard$', 'dashboard', name='dashboard'),
                       url(r'^uiform/(?P<pk>[0-9]*)$', 'uiform_detail', name='uiform_detail'),
                       url(r'^uiform/(?P<pk>[0-9]*)/fields/new$', UIFormFieldCreateView.as_view(), name='uiformfield_new'),
                       url(r'^uiform/(?P<formpk>[0-9]*)/fields/(?P<fieldpk>[0-9]*)$', UIFormFieldUpdateView.as_view(), name='uiformfield_edit'),

                       # Site root
                       url(r'^$', 'index', name='index')
                       )
