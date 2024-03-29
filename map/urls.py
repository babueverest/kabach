from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from mymap.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #(r'^$', TemplateView.as_view(template_name='index.html')),
    (r'^$', index),
    (r'^push$',push_in_db),
    # Examples:
    # url(r'^$', 'map.views.home', name='home'),
    # url(r'^map/', include('map.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
