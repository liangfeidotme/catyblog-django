from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog.views',
    url(r'^$', 'index', {'cat_name': 'home'}),
    #url(r'^json/(?P<json_type>\w+)/', 'json_gate_way', name="json_gate_way"),

    url(r'^category/(?P<cat_name>\w+)/$', 'index', name='category'),
    url(r'^category/(?P<cat_name>\w+)/page/(?P<page_num>\d+)/$', 'index', name='page'),

    url(r'^article/(?P<article_id>\d+)/$', 'article', name='article'),

    url(r'^archive/(?P<published_on>\d{4}-\d{2})/$', 'archive', name='archive'),

    url(r'^tag/(?P<tag_name>\w+)/$', 'tag', name='tag'),
)
