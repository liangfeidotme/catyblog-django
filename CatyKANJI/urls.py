from django.conf.urls import patterns, include, url

urlpatterns = patterns('CatyKANJI.views',
    url(r'^$', 'index'),
    url(r'^download/$', 'download_kanji'),
    url(r'^download/(?P<version>\d+)$', 'download_kanji'),
    url(r'^test/$', 'test'),
)
