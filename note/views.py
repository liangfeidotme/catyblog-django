# -*- coding: utf-8 -*-
from django.shortcuts import render
from note.mongo import insert_issue, get_issue
# Create your views here.


def index(request):
    # data_dict = get_issue()
    # data_dict['nav_name'] = 'note'
    # return render(request, 'note/index.html',
    #     {
    #         'nav_name': 'note',
    #         'one_note': data_dict
    #     })

    return render(request, 'note/index.html',
        {
            'nav_name': 'note',
        })