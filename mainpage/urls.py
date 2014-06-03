'''
Created on 2013-4-13

@author: zhaosong
'''
from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',   
    url(r'^$', views.index), 
    url(r'^time/$', views.current_datetiem),
    url(r'^time/(\d{1,2})/$', views.current_hour),
)