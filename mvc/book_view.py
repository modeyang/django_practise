'''
Created on 2013-4-11

@author: computer
'''
 

from django.http import HttpResponse, Http404, HttpResponseNotAllowed
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from mvc.models import Book, Choice
from django.template import RequestContext

def index(request):
    if request.siteuser is None:
        return Http404
        
    books = Book.objects.all().order_by('pub_date')[:10]
    return render_to_response("mvc/book_index.html", {"books": books})

def details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render_to_response("mvc/details.html", {"book":book},
                              context_instance=RequestContext(request))

def results(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render_to_response("mvc/results.html", {"book":book})

def votes(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    try:
        selected_choice = book.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render_to_response("mvc/details.html", {"book":book,
                                 "error_msg":"you don't get a choice"},
                                 context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button. 
        return HttpResponseRedirect(reverse('book_results', args=(book.id, )))
