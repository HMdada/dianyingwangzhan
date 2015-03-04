from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'yingchong.views.home'),
    url(r'^index1.html$', 'yingchong.views.index1'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
    	{'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
    url(r'^admin/', include(admin.site.urls)),
)
