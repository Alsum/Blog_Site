from django.conf.urls.defaults import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import blog.urls
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

     url(r'^admin/', include(admin.site.urls)),
     url(r'^blog/',include(blog.urls)),
	 url(r'^media/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
     
)
