#! usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from django.http import HttpResponse


def graph(request):
    
    x = np.linspace(-20.0, 20.0, 100000)
    y = np.sin(x) / x
    
    fig = plt.figure()
    axis = plt.subplot(111)
    axis.plot(x,y)
    
    response = HttpResponse(content_type='image/png')
    plt.savefig(response, format='png')
    
    return response
