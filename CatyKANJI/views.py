# -*- coding: utf-8 -*-
import os
import json
from django.http import HttpResponse

from mongo import KanjiMongo


# Create your views here.

_mongo = KanjiMongo()


def index(request):
    return HttpResponse('hello world')

def download_kanji(request):
    kanji = _mongo.get_kanji()
    return HttpResponse(kanji, content_type="application/json")
