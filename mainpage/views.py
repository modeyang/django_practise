
# from django.shortcuts import  render
from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response

# from models import Book

import datetime

def index(request):
    return HttpResponse("welcome to my blog")

def current_datetiem(request):
    now = datetime.datetime.now()
    return render_to_response('static/test.html', {'now':now})

def current_hour(request, offset):
    offset = int(offset)
    now = datetime.datetime.now()
    dt = now + datetime.timedelta(hours=offset)
    t = get_template('static/test.html')
    html = t.render(Context({'now': dt}))
    return HttpResponse(html)
    