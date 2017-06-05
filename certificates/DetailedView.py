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
    Cert_InterimCSSE = TableCAFSC.objects.filter(ShipMainData=ShipName).order_by('-CertState', '-DocCreated')
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
        print (ShipName.Type)
        context['ShipType']= ContextShipType[ShipName.Type]
        Counts = {}
        for i in ContextData:
            iModel = ContextData[i]['ModelName']
            CertDraftCount = iModel.objects.filter(ShipMainData=ShipName, CertState='d').count()
            CertConfmCount = iModel.objects.filter(ShipMainData=ShipName, CertState='c').count()
            CertDeactCount = iModel.objects.filter(ShipMainData=ShipName, CertState='x').count()
            Counts[i] = ContextData[i]['CertName'], CertDraftCount, CertConfmCount, CertDeactCount
        context['Counts'] = Counts
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


@method_decorator(login_required(login_url="/in/login/"), name='dispatch')
class CertDetailView(DetailView):
    def get_context_data(self, **kwargs):
        CertStop = None
        CertData = ContextData[self.kwargs['cert_id']]['ModelName']


        # print(ContextCCSMC['ModelName'])
        Certificate = CertData.objects.get(pk=self.kwargs['pk'])
        CertFilter = CertData.objects.filter(ShipMainData_id=Certificate.ShipMainData.pk)
        context = super(CertDetailView, self).get_context_data(**kwargs)
        context['CertType'] = CertType[Certificate.CertType]
        context['CertState'] = CertState[Certificate.CertState]
        for Certificates in CertFilter:
            if Certificates.CertState == "c":
                context['CertStop'] = "stop"

        context['now'] = timezone.now()
        context['Certificate'] = Certificate
        context['CertName'] = ContextData[self.kwargs['cert_id']]['CertName']
        context['Cert'] = str(self.kwargs['cert_id'])
        return context

    def get_object(self, queryset=None):
        return

    def get_template_names(self):
        # return 'pages/view-'+TemplateTable[self.kwargs['cert_id']]
        return 'pages/view-certificate-details.html'