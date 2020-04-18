from django.contrib import admin

from .models import Tovar, Group, Tag

admin.site.register(Tovar)
admin.site.register(Group)
admin.site.register(Tag)

