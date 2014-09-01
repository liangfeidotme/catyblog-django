__author__ = 'lyndon'

from django.shortcuts import render
from blog.views import fill_page_with


def about(request):
    return render(request, 'about.html',
                  fill_page_with(nav_name='about'))


def contact(request):
    return render(request, 'contact.html',
                  fill_page_with(nav_name='contact'))