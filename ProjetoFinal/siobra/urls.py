#from django.conf.urls.defaults import *
from django.conf.urls import url
from . import views
from siobra import views


urlpatterns = [
    url(r'^$', views.index, name='index'), #, name='index'
	url(r'^siobra/', views.index, name='index'),
	#url(r'^contact/$', views.contact,name='contact'), #, name='contact'
	url(r'^home/$', views.index,name='index'), #, name='contact'
	#url(r'^/siobra/$', views.contact), #, name='contact'
]
