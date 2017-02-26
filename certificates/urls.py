from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views, DetailedView
from .views import *

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^add-new/', views.add_new, name='add-new'),
    url(r'^ships/view-all/', views.IndexView.as_view(), name='view-all'),
    url(r'^ships/(?P<id>\d+)/$', DetailedView.view_detail, name='view_detail'),
    url(r'^(?P<id>\d+)/edit/(?P<ld>\d+)/$', views.edit, name='edit'),
    url(r'^(?P<ship_id>\d+)/form/$', CertificateView.as_view(), name='form_view'),
    # url(r'^(?P<id>\d+)/False/$', views.view_detail, name='view_detail'),
    url(r'^login/$', auth_views.login, {'template_name': 'pages/login.html'}, name='login'),
	url(r'^logout/', views.logout, name='logout'),
    url(r'^$', views.index, name='index'),


]