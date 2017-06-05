from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout as django_logout
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView
from django.forms import BaseModelFormSet
from django.views.generic.edit import CreateView
from django.views.decorators.http import condition
from django.views.generic.edit import FormMixin
from django.views.generic.edit import UpdateView


from .ContextData import *


@method_decorator(login_required(login_url="/in/login/"), name='dispatch')
class CreateCertificateView(CreateView):

    def get_form_class(self, **kwargs):
        """
        Returns an instance of the form to be used in this view.
        kwarg from database
         """
        return ContextData[self.kwargs['cert_id']]['FormName']

    def get_template_names(self, **kwargs):
        ShipID = self.request.GET.get('shipid')
        ModelObject = ContextData[self.kwargs['cert_id']]['ModelName']
        # if str(ModelObject.objects.filter(CertState='c', ShipMainData__pk=ShipID)) == '<QuerySet []>':
        #     return 'pages/create-'+ContextData[self.kwargs['cert_id']]['TemplateName']
        # else:
        #     return 'pages/active-certificate-error.html'
        return 'pages/certificate-base-form.html'

    def get_form(self, form_class=None):
        form = super(CreateCertificateView, self).get_form()
        return form

    def form_valid(self, form, **kwargs):
        ShipID = self.request.GET.get('shipid')
        form.instance.DocAuthor = self.request.user
        form.instance.ShipMainData = ShipMainData.objects.get(id=ShipID)
        form.instance.CertState = 'd'
        return super(CreateCertificateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateCertificateView, self).get_context_data(**kwargs)
        ShipID = self.request.GET.get('shipid')
        context['CertName'] = ContextData[self.kwargs['cert_id']]['CertName']
        context['TemplateName'] = 'forms/update/update-'+ContextData[self.kwargs['cert_id']]['TemplateName']
        context['State'] = "Create New Certificate"
        context['ButtonState'] = "Add"
        context['ShipName'] = ShipMainData.objects.get(id=ShipID)
        return context

@method_decorator(login_required(login_url="/in/login/"), name='dispatch')
class UpdateCertificateView(UpdateView):
    queryset = None

    def get_form_class(self, **kwargs):
        """
        Returns the form class to use in this view
        """
        return ContextData[self.kwargs['cert_id']]['FormName']

    def get_queryset(self, **kwargs):
        """
        Return the `QuerySet` that will be used to look up the object.
        Note that this method is called by the default implementation of
        `get_object` and may not be called if `get_object` is overridden.
        """
        ModelObject = ContextData[self.kwargs['cert_id']]['ModelName']
        return ModelObject.objects.all()

    def get_template_names(self, **kwargs):
        """
        Returns a list of template names to be used for the request. Must return
        a list. May not be called if render_to_response is overridden.
        """
        ModelObject = ContextData[self.kwargs['cert_id']]['ModelName']
        ModelObject = ModelObject.objects.get(pk=self.kwargs['pk'])
        if ModelObject.CertState=='d':
            return 'pages/certificate-base-form.html'
            # return 'forms/update/update-'+ContextData[self.kwargs['cert_id']]['TemplateName']
        else:
            return 'pages/form-error-update.html'

    def form_valid(self, form):
        form = self.get_form()
        form.save()
        return super(UpdateCertificateView, self).form_valid(form)

    def get_success_url(self):
        return "../"

    def post(self, request, *args, **kwargs):
        request.POST = (request.POST.copy())
        ModelObject = ContextData[self.kwargs['cert_id']]['ModelName']
        Certificate = ModelObject.objects.get(pk=self.kwargs['pk'])
        CertFilter = ModelObject.objects.filter(ShipMainData_id=Certificate.ShipMainData.id)
        State = 'c'
        for Certificates in CertFilter: #Check simultaneous confirmation of multiple certificates
            if Certificates.CertState == "c":
                State = 'd'
        if 'save' in request.POST: #Check before editing or saving confirmed certificates
            form = self.get_form()
            if Certificate.CertState != "c":
                return super(UpdateCertificateView, self).post(request, *args, **kwargs)
            else:
                return HttpResponseRedirect('../')  # change to redirect
        if 'confirm' in request.POST:
            ModelObject.objects.filter(pk=self.kwargs['pk']).update(CertState=State)
            return HttpResponseRedirect('../')  # change to redirect
        if 'deactivate' in request.POST:
            ModelObject.objects.filter(pk=self.kwargs['pk']).update(CertState='x')
            return HttpResponseRedirect('../') #change to redirect

    def get_context_data(self, **kwargs):
        context = super(UpdateCertificateView, self).get_context_data(**kwargs)
        CertData = ContextData[self.kwargs['cert_id']]['ModelName']
        Certificate= CertData.objects.get(pk=self.kwargs['pk'])
        context['CertName'] = ContextData[self.kwargs['cert_id']]['CertName']
        context['TemplateName'] = 'forms/update/update-'+ContextData[self.kwargs['cert_id']]['TemplateName']
        context['State'] = "Edit Certificate"
        context['ButtonState'] = "Update"
        context['ShipName'] = Certificate.ShipMainData
        return context