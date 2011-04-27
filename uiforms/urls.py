from django.conf.urls.defaults import *

urlpatterns = patterns('uiforms.views',
                       url(r'^register$', 'user_register', name='user_register'),
                       url(r'^login$', 'user_login', name='user_login'),
                       url(r'^logoff$', 'user_logoff', name='user_logoff'),
                       url(r'^dashboard$', 'dashboard', name='dashboard'),

                       # Site root
                       url(r'^$', 'index', name='index')
                       )
