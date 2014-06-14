from django.shortcuts import render


def index(request):
    return render(request, 'publish/index.html')


def write(request):
    return render(request, 'publish/write.html')


def archive(request):
    return render(request, 'publish/archive.html')