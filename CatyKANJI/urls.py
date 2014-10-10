from django.conf.urls import patterns, include, url

urlpatterns = patterns('CatyKANJI.views',
    url(r'^$', 'index'),
    url(r'^download/$', 'download_kanji')
)
