#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django import forms


class LoginForm(forms.Form):
    login = forms.CharField(label='Login')
    password = forms.CharField(label='Password')
    
