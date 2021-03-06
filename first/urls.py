from django.conf.urls import patterns, include, url
from django.contrib import admin
from first.views import fest_details,home,savefest,saveuser,saveevent,contactus

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home, name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^fest/(\d+)$', fest_details),
    url(r'^savefest/$', savefest),
    url(r'^saveuser/$', saveuser),
    url(r'^saveevent/$', saveevent),
    url(r'^contactus/$', contactus),

)
