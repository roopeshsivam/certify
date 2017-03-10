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
    # url(r'^ships/', views.myModel_asJson, name='my_ajax_url'),
    url(r'^ships/', views.ShipIndexView.as_view(), name='ship-view-all'),
    url(r'^owners/', views.OwnerIndexView.as_view(), name='owner-view-all'),
    url(r'^ship/(?P<id>\d+)/$', DetailedView.view_detail, name='view_detail'),
    url(r'^(?P<id>\d+)/edit/(?P<ld>\d+)/$', views.edit, name='edit'),
    url(r'^(?P<ship_id>\d+)/(?P<cert_id>[a-zA-Z]{5})/$', CreateCertificateView.as_view(), name='form_view'),
    # url(r'^(?P<id>\d+)/False/$', views.view_detail, name='view_detail'),
    url(r'^login/$', auth_views.login, {'template_name': 'pages/login.html'}, name='login'),
	url(r'^logout/', views.logout, name='logout'),
    url(r'^$', views.index, name='index'),


]