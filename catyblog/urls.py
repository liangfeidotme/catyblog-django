from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('catyblog.views',
    url(r'^$', include('blog.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^about/', 'about', name='about'),
    url(r'^admin/', include(admin.site.urls)),
)  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

