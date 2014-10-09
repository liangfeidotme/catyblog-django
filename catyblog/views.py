# -*- coding: utf-8 -*-
__author__ = 'lyndon'

from django.shortcuts import render
from django.http import HttpResponse
from blog.views import fill_page_with

import json

def about(request):
    return render(request, 'about.html',
                  fill_page_with(nav_name='about'))


def contact(request):
    return render(request, 'contact.html',
                  fill_page_with(nav_name='contact'))

def catykanji_contents(request):
    if request.method == 'GET':
        contents = {}
        contents['character'] = '鬱'
        contents['pronunciation'] = 'うつ'
        contents['phrases'] = '鬱病'

        return HttpResponse(json.dumps(contents), content_type='application/json')
