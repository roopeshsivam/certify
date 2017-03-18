from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout as django_logout
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import *
from django.views.generic import DetailView



@login_required(login_url="/certificates/login/")
def view_detail(request, id):
	ShipName = get_object_or_404(ShipMainData.objects, pk=id)
	Cert_InterimCSSE = CertCSSE.objects.filter(ShipMainData=ShipName).order_by('-CertState', '-DocCreated')
	# InterimCSSEActive = InterimCSSE.objects.filter(ShipMainData__pk=id).filter(IsActive=True)
	# InterimCSSEInActive = InterimCSSE.objects.filter(ShipMainData__pk=id).filter(IsActive=False)
	# InterimCSSEInActive = ShipMainData.objects.get(interimcsse=ShipName)
	# apple = IntrimCSSE.get_url
	# apple= InterimCSSE.get_url(id,id)
	# print (apple)
	context = {
		"ShipName": ShipName,
		"Cert_InterimCSSE" : Cert_InterimCSSE,
	}
	return render(request, 'pages/view-details.html', context)

class CertDetailView(DetailView):

	model = CertCSSE

	def get_context_data(self, **kwargs):
		context = super(CertDetailView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context

	def get_template_names(self):
		ManagerObject = CertViewManager.objects.get(FieldName=self.kwargs['cert_id'])
		ModelObject = ModelTable[ManagerObject.FieldName]
		ModelObject = ModelObject.objects.get(pk=self.kwargs['pk'])
		return ManagerObject.DetailTemplateName
