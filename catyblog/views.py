__author__ = 'lyndon'

from django.shortcuts import render
from blog.views import get_archive, article_count_per_category


def about(request):
    return render(request, 'about.html',
              {
                  'nav_name': 'about',
                  'archive': get_archive(),
                  'categories': article_count_per_category(),
              })


def contact(request):
    return render(request, 'contact.html',
              {
                  'nav_name': 'contact',
                  'archive': get_archive(),
                  'categories': article_count_per_category(),
              })