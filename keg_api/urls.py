from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'keg_api.views.index', name='index'),
    url(r'^v1/start_pour/(?P<volume>\d+)/(?P<user_id>\d+)/$', 'keg_api.views.start_pour', name='start_pour'),
    url(r'^v1/stop_pour/', 'keg_api.views.stop_pour', name="stop_pour"),
    url(r'^v1/pour_status/(?P<pour_id>\d+)/$', 'keg_api.views.pour_status', name='pour_status'),
    url(r'^v1/authenticate/(?P<sso>\d+)/$', 'keg_api.views.authenticate', name='authenticate'),
    url(r'^v1/system_info/', 'keg_api.views.system_info', name="system_info"),
    url(r'^v1/pour_history/', 'keg_api.views.pour_history', name="pour_history"),
    url(r'^v1/user_info/(?P<user_id>\d+)/$', 'keg_api.views.user_info', name="user_info"),
    url(r'^v1/user_photo/(?P<user_id>\d+)/$', 'keg_api.views.user_photo', name="user_photo"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
