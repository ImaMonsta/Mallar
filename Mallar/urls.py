from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Mallar.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('muser.urls')),
    url(r'^$', 'main.views.home', name='mallar_home')
)


urlpatterns += patterns(
    'django.contrib.auth.views',

    url(r'^login/$', 'login',
        {'template_name': 'login.html'},
        name='mallar_login'),

    url(r'^logout/$', 'logout',
        {'next_page': 'mallar_home'},
        name='mallar_logout'),
)
