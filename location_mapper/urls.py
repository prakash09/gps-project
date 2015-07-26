from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('location_mapper.views',

    url(r'^get-location/$', 'get_location', name='get_location'),
    url(r'^get_vehicle/$', 'get_vehicle', name='get_vehicle'),


)
