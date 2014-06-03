from django.conf.urls import patterns, include, url
from django.conf import settings

import mvc, mainpage, Photo

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'mainpage.views.index'),
    url(r'^mainpage/', include('mainpage.urls')),
    url(r'^book/', include('mvc.urls')),
    url(r'^photo/', include('Photo.urls')),
    url(r'^Blog/', include('Blog.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
    # url(r'',  include('social_login.urls'))
)

if settings.DEBUG:
	urlpatterns += patterns('',
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
	)

# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# urlpatterns += staticfiles_urlpatterns()
