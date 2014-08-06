from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog.views_publish',
    url('^$', 'index', name='index'),
    url('^write/$', 'write', name='publish_write'),
    url('^archive/$', 'archive', name='publish_archive'),
    url('^backup/$', 'backup', name='backup')
)
