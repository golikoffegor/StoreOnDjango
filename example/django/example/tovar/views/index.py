from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from ..models import Tovar


def index(request):
    
    fmt = request.GET.get('format','html').lower()
    if fmt == 'xml':
        template_name = 'tovar/index.xml'
        resp_type = 'text/xml'
    elif fmt == 'json':
        template_name = 'tovar/index.json'
        resp_type = 'text/json'
    else:
        template_name = 'tovar/index.html'
        resp_type = 'text/html; charset=utf-8'
    
    all_tovars = Tovar.objects.all()
    template = loader.get_template(template_name)
    text = template.render(locals(), request)
    
    return HttpResponse(text, content_type=resp_type)


    

