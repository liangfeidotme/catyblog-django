__author__ = 'lyndon'

from django.shortcuts import render


def about(request):
    return render(request, 'about.html', {'nav_name': 'about'})


def contact(request):
    return render(request, 'contact.html', {'nav_name': 'contact'})