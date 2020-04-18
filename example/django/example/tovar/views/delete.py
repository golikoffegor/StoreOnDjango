#!/usr/bin/env python3
# -*- coding: utf-8 -*

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from ..models import Tovar

def delete(request, id_tovar):
    tovar = get_object_or_404(Tovar, pk=id_tovar)
    tovar.delete()
    return HttpResponseRedirect(reverse('tovar:index'))
