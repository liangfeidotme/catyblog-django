# -*- coding: utf-8 -*-
from django.http import HttpResponse

from mongo import KanjiMongo


# Create your views here.

_mongo = KanjiMongo()


def index(request):
    return HttpResponse('hello world')

def download_kanji(request):
    kanji = _mongo.get_kanji()
    return HttpResponse(kanji, content_type="application/json")

def test(request):
    return HttpResponse(_mongo.test(), content_type="application/json; charset=utf-8")
