# -*- coding: utf-8 -*-

from django import forms
from .models import Tovar


class PictureForm(forms.Form):
    picture = forms.FileField(label='картинка')


class TagListForm(forms.Form):
    tag_list = forms.CharField(label='новые', required=False)


class TovarForm(forms.Form):
    
    title = forms.CharField(label='Наименование', max_length=256)
    article = forms.CharField(label='Артикул', max_length=16)
    quantity = forms.IntegerField(label='В наличии', min_value=0)
    description = forms.CharField(label='Описание', widget=forms.Textarea, required=False)
    
class TovarModelForm(forms.ModelForm):
    class Meta:
        model = Tovar
        fields = ['title', 'article', 'quantity', 'description']
    
