from django.conf.urls import patterns, include, url

urlpatterns = patterns('muser.views',
    url(r'^home$', 'home', name='muser_home')
)