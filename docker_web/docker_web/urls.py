from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'docker_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', 'web_site.views.index', name='index'),
    url(r'^ajaximages/$', 'web_site.views.ajaximages', name='ajaximages'),
    url(r'^login/$', 'auth_models.views.login', name='login'),
    url(r'^logout/$', 'auth_models.views.logout', name='logout'),
    url(r'^containers/$', 'web_site.views.containers'),
    #url(r'^ajaxcontainers/$', 'web_site.views.ajaxcontainers'),
    url(r'^host/$', 'web_site.views.host'),
    url(r'^checkhost/$', 'web_site.views.checkhost'),
)
