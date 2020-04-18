#!/usr/bin/env python3
# -*- coding: utf-8 -*

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from ..forms import TovarModelForm
from ..models import Tovar

from restful import restful

@restful
def create(request):
    
    tovar = Tovar()
    form = TovarModelForm(instance=tovar)
    
    return render(request, 'tovar/tovar_edit.html', locals() )

@create.method('POST')
def create(request):
    tovar = Tovar()
    form = TovarModelForm(request.POST, instance=tovar)
    if form.is_valid():
        tovar = form.save()
        return HttpResponseRedirect(reverse('tovar:show', args=[tovar.pk]))
    else:
        return render(request, 'tovar/tovar_edit.html', locals())
    
        
        
    
