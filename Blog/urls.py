'''
Created on 2013-7-9

@author: yanggx
'''

from django.conf.urls import patterns, url
import views
# from models import Book, Choice
from django.views.generic import DetailView, ListView

urlpatterns = patterns('Blog.views',
    url(r'^$', 'blog_list', name='bloglist'),
    url(r'(?P<id>\d+)/$', 'blog_show', name='detailblog'),
    url(r'^tag/(?P<id>\d+)/$', 'blog_filter', name='filtrblog'),
    url(r'^add/$', 'blog_add', name='addblog'),
)