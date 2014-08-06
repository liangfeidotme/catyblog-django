from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'publish/index.html')


def write(request):
    return render(request, 'publish/write.html')


def archive(request):
    return render(request, 'publish/archive.html')


def backup(request):
    from lyndondb import CatyBlogDB
    CatyBlogDB().backup_mysql()
    return HttpResponse('Thanks')