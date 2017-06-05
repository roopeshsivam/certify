from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views, DetailedView, IndexedView, CreateCertView
from .views import *

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^add-new/', views.add_new, name='add-new'),

    url(r'^ships/', IndexedView.ShipIndexView.as_view(), name='ship-view-all'),
    url(r'^ship/(?P<pk>\d+)/$', DetailedView.ShipDetailView.as_view(), name='ship_detailed'),
    url(r'^ship/(?P<id>\d+)/edit$', DetailedView.view_detail, name='view_detail'),
    url(r'^ship/(?P<id>\d+)/delete', DetailedView.view_detail, name='view_detail'),

    url(r'^own/(?P<pk>\d+)/$', DetailedView.OwnerDetailView.as_view(), name='owner_detailed'),
    url(r'^own/(?P<id>\d+)/edit/$', DetailedView.OwnerDetailView.as_view(), name='owner_view_detail'),
    url(r'^own/(?P<id>\d+)/delete/$', DetailedView.OwnerDetailView.as_view(), name='owner_view_detail'),

    url(r'^cert/(?P<cert_id>[a-z]{5})/create/$', CreateCertView.CreateCertificateView.as_view(), name='form_view'),
    url(r'^cert/(?P<cert_id>[a-z]{5})/(?P<pk>\d+)/$', DetailedView.CertDetailView.as_view(), name='index'),
    url(r'^cert/(?P<cert_id>[a-z]{5})/(?P<pk>\d+)/edit/$', CreateCertView.UpdateCertificateView.as_view(), name='form_update'),
    url(r'^cert/(?P<cert_id>[a-z]{5})/(?P<pk>\d+)/print/$', CreateCertView.UpdateCertificateView.as_view(), name='form_update'),

    url(r'^own/', IndexedView.OwnerIndexView.as_view(), name='owner-view-all'),
    url(r'^cert/(?P<cert_id>[a-z]{5})/$', IndexedView.CertIndexView.as_view(), name='cert-index'),

    url(r'^login/$', auth_views.login, {'template_name': 'pages/login.html'}, name='login'),
	url(r'^logout/', views.logout, name='logout'),
    url(r'^$', views.index, name='index'),
]