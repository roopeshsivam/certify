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



@login_required(login_url="/certificates/login/")
def view_detail(request, id):
	ShipName = get_object_or_404(ShipMainData.objects, pk=id)
	Cert_InterimCSSE = CertCSSRTC.objects.filter(ShipMainData=ShipName).order_by('-CertState', '-DocCreated')
	context = {
		"ShipName": ShipName,
		"Cert_InterimCSSE" : Cert_InterimCSSE,
	}
	return render(request, 'pages/view-details.html', context)




@method_decorator(login_required(login_url="/in/login/"), name='dispatch')
class ShipDetailView(DetailView):
	model = ShipMainData
	def get_context_data(self, **kwargs):
		ShipName = ShipMainData.objects.get(pk=self.kwargs['pk'])
		context = super(ShipDetailView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		context['ShipName'] = ShipName
		context['CertCSSRTC'] = CertCSSRTC.objects.filter(ShipMainData=ShipName).order_by('-CertState', '-DocCreated')
		return context

	def get_template_names(self):
		return 'pages/ship-view-details.html'

@method_decorator(login_required(login_url="/in/login/"), name='dispatch')
class OwnerDetailView(DetailView):
	model = ShipOwner
	def get_context_data(self, **kwargs):
		OwnerName = ShipOwner.objects.get(pk=self.kwargs['pk'])
		context = super(OwnerDetailView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		context['OwnerName'] = OwnerName
		return context

	def get_template_names(self):
		return 'pages/owner-view-details.html'


class CertDetailView(DetailView):
	def get_context_data(self, **kwargs):
		CertData = ModelTable[self.kwargs['cert_id']]
		Certificate = CertData.objects.get(pk=self.kwargs['pk'])
		context = super(CertDetailView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		context['Certificate'] = Certificate
		context['CertState'] = CertState[Certificate.CertState]
		context['CertType'] = CertType[Certificate.CertType]
		context['CertName'] = CertName[self.kwargs['cert_id']]
		return context

	def get_object(self, queryset=None):
		return

	def get_template_names(self):
		# return 'pages/view-'+TemplateTable[self.kwargs['cert_id']]
		return 'pages/view-certificate-details.html'