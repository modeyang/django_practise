'''
Created on 2013-4-13

@author: yanggenxing
'''
from django.conf.urls import patterns, url
import views, book_view
from models import Book, Choice
from django.views.generic import DetailView, ListView


# book items url  
urlpatterns = patterns('',  
    url(r'^$', 
        ListView.as_view(
                queryset=Book.objects.all().order_by('pub_date')[:10],
                context_object_name="books",
                template_name="mvc/book_index.html")),
#     url(r'^$', book_view.index), 
#     url(r'^(?P<book_id>\d+)/$', book_view.details), 
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Book,
            template_name='mvc/details.html')),                     
    url(r'^(?P<pk>\d+)/results/$',
        DetailView.as_view(
            model=Book,
            template_name='mvc/results.html'),
        name='book_results'),
#     url(r'^(?P<book_id>\d+)/results/$', book_view.results),
    url(r'^(?P<book_id>\d+)/votes/$', book_view.votes),
)