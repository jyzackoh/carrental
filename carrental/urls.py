from django.conf.urls import patterns, include, url
from . import views
from django.contrib import admin
from django.contrib.auth.views import login, logout
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'carrental.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index),
    url(r'^search/$', views.search),
    url(r'^car/$', views.car_info),
    url(r'^rent/$', views.rent),
    url(r'^rent/auth/$', login, {'extra_context':{'rent_error':'Please Login to Rent a car!'}}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/user/$', views.account),
    url(r'^accounts/user/([A-Za-z]+)/$', views.account_public),
    url(r'^accounts/modify/$', views.modify),
    url(r'^accounts/register/$',  views.register),
    url(r'^accounts/login/$',  login),
    url(r'^accounts/logout/$', logout, {'next_page': '/'}),
)