#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from textwrap import dedent
from django.shortcuts import get_object_or_404, render
from django.db import connection
from ..models import Tovar, Tag
from ..forms import TagListForm
from restful import restful


@restful
def tags(request, id_tovar):
    tovar = get_object_or_404(Tovar, pk=id_tovar)
    form = TagListForm()
    return render(request, 'tovar/tags.html', locals())

@tags.method('POST')
def tags(request, id_tovar):
    form = TagListForm(request.POST)
    if form.is_valid():
        tag_list = form.cleaned_data['tag_list']
        tag_list = tag_list.split(',')
        tag_list = map(str.strip, tag_list)
        tag_list = map(str.lower, tag_list)
        with connection.cursor() as cursor:
            for pk_tag in tag_list:
                cursor.execute(dedent('''\
                    insert into tovar_tag ( title )
                       values ( %s )
                       on conflict do nothing ;'''), 
                    [ pk_tag ] 
                )
                cursor.execute(dedent('''\
                    insert into tovar_tovar_tags ( tovar_id, tag_id )
                       values ( %s, %s )
                       on conflict do nothing ;'''),
                    [ id_tovar, pk_tag ] 
                )                
    tovar = get_object_or_404(Tovar, pk=id_tovar)
    return render(request, 'tovar/tags.html', locals())




def tags_post_для_ламеров(request, id_tovar):
    form = TagListForm(request.POST)
    if form.is_valid():
        tag_list = form.cleaned_data['tag_list']
        tovar = get_object_or_404(Tovar, pk=id_tovar)
        for pk_tag in map(str.strip,tag_list.split(',')):
            pk_tag = pk_tag.lower()
            try:
                tag = Tag.objects.get(pk=pk_tag)
            except Tag.DoesNotExist:
                tag = Tag(title=pk_tag)
                tag.save()
            tovar.tags.add(tag)
        tovar.save()
    return render(request, 'tovar/tags.html', locals())
