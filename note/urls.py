__author__ = 'lyndon'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('note.views',
    url(r'^$', 'index', name='index'),
)
