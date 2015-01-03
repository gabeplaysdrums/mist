from django.conf.urls import patterns, url


urlpatterns = patterns('studio.views',
    url(r'^$', 'home'),
    url(r'^tests/$', 'tests'),
)
