from django.shortcuts import render, get_object_or_404

from ..models import Tovar


def show(request, id_tovar):
    
    tovar = get_object_or_404(Tovar, pk=id_tovar)
    tags = ', '.join(( tag.title for tag in tovar.tags.all() ))
    
    return render(request, 'tovar/tovar_show.html', locals())

