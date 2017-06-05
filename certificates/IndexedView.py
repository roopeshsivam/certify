from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout as django_logout
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator


from .models import *
from .ContextData import *
from django.views.generic import DetailView


@method_decorator(login_required(login_url="/in/login/"), name='dispatch')
class ShipIndexView(generic.ListView):
    """docstring for IndexView"""
    template_name = 'pages/ship-view-all.html'
    context_object_name = 'ObjectList'

    def get_queryset(self, **kwargs):
        owner = self.request.GET.get('owner')
        if owner is not None:
            return ShipMainData.objects.filter(Owner_id=owner)
        else:
            return ShipMainData.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ShipIndexView, self).get_context_data(**kwargs)
        owner = self.request.GET.get('owner')
        if owner is not None:
            context['OwnerName'] = ShipOwner.objects.get(id=owner)
            context['UserName'] = self.request.user.get_full_name()
        return context


@method_decorator(login_required(login_url="/in/login/"), name='dispatch')
class OwnerIndexView(generic.ListView):
    """docstring for IndexView"""
    template_name = 'pages/owner-view-all.html'
    context_object_name = 'ObjectList'

    def get_queryset(self, **kwargs):
        return ShipOwner.objects.all()


@method_decorator(login_required(login_url="/in/login/"), name='dispatch')
class CertIndexView(generic.ListView):
    """docstring for IndexView"""
    template_name = 'pages/cert-view-all.html'

    def get_queryset(self, **kwargs):

         return

    def get_context_data(self, **kwargs):
        CertData = ContextData[self.kwargs['cert_id']]['ModelName']
        context = super(CertIndexView, self).get_context_data(**kwargs)
        ship = self.request.GET.get('shipid')
        print (CertData)
        context['CertName'] = CertData.objects.filter(ShipMainData_id=ship).order_by("CertState")
        context['UserName'] = self.request.user.get_full_name()
        context['CertficateName'] = ContextData[self.kwargs['cert_id']]['CertName']
        return context