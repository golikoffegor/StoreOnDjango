#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class restful(object):
    
    def __init__(self, get_function=None):
        self.__Methods = dict()
        if get_function is not None:
            self.__Methods['GET'] = get_function
    
    def method(self, name):
        def register(function):
            self.__Methods[name.upper()] = function
            return self
        return register
    
    def __call__(self, request, *args, **kwargs):
        method = self.__Methods[request.method.upper()]
        return method(request, *args, **kwargs)

    
        
