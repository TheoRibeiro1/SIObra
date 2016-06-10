"""ProjetoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns,include, url
from django.contrib import admin
#from django.conf.urls.defaults import *
#from siobra.models import Entry
#from tagging.views import tagged_object_list
from siobra import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('siobra.urls')),
    url(r'^home/', include('siobra.urls')),
    url(r'^siobra/', include('siobra.urls')),
    url(r'^contact/$', views.contact,name='contact'),
    #url(r'^contact/', include('siobra.urls')),
    #url(r'^$', include('siobra.urls')),
    #url(r'^siobra/', include('siobra.urls')),
)
#urlpatterns = patterns('django.views.generic.date_based',

 #   (r'(?P<year>d{4})/(?P<month>[a-z]{3})/(?P<day>w{1,2})/(?P<slug>[-w]+)/$', 'object_detail', dict(info_dict, slug_field='slug',template_name='blog/detail.html')),
 #   (r'^(?P<year>d{4})/(?P<month>[a-z]{3})/(?P<day>w{1,2})/(?P<slug>[-w]+)/$', 'object_detail', dict(info_dict, template_name='blog/list.html')),
 #   (r'^(?P<year>d{4})/(?P<month>[a-z]{3})/(?P<day>w{1,2})/$','archive_day',dict(info_dict,template_name='blog/list.html')),
 #   (r'^(?P<year>d{4})/(?P<month>[a-z]{3})/$','archive_month', dict(info_dict, template_name='blog/list.html')),
 #   (r'^(?P<year>d{4})/$','archive_year', dict(info_dict, template_name='blog/list.html')),
 #   (r'^$','archive_index', dict(info_dict, template_name='blog/list.html')),
#)
