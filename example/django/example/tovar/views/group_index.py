from django.shortcuts import render

from ..models import Group


def group_index(request):
    
    all_groups = Group.objects.all()
    
    return render(request, 'tovar/allgroups.html', locals())

