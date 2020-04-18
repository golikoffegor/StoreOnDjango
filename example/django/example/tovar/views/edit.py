from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from restful import restful
from ..models import Tovar
from ..forms import TovarModelForm

import sys

@restful
def edit(request, id_tovar):
    
    tovar = get_object_or_404(Tovar, pk=id_tovar)
    form = TovarModelForm(instance=tovar)
        
    return render(request, 'tovar/tovar_edit.html', locals())


@edit.method('POST')
def edit(request, id_tovar):
    
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('tovar:index'))
    if not request.user.is_superuser:
        if not request.user.has_perm('tovar.change_tovar'):
            return HttpResponseRedirect(reverse('tovar:index'))
    
    raw_data = dict()
    raw_data.update( request.POST )
    
    tovar = get_object_or_404(Tovar, pk=id_tovar)
    
    form = TovarModelForm(request.POST, instance=tovar)
    if form.is_valid():
        form.save()
        return render(request, 'tovar/tovar_show.html', locals())
    else:
        
        return render(request, 'tovar/tovar_edit.html', locals())
