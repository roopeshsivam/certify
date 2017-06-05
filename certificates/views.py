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





from .models import *
from .forms import *
from .ContextData import *

# from certificates.models import CertViewManager

# Create your views here.


@login_required(login_url="login/")
def index(request):
    return render(request, 'pages/index.html')


@login_required(login_url="/certificates/login/")
def add_new(request):
    # ShipForm = ShipFormHead(request.POST or None)
    # if ShipForm.is_valid():
    # 	instance = ShipForm.save(commit=False)
    # 	instance.save()
    # context = {
    #  	"ShipForm": ShipForm
    #  }
    return render(request, 'pages/add-new.html')


@login_required(login_url="/in/login/")
def view_all(request):
    return render(request, 'pages/view-all.html')


@login_required(login_url="/in/login/")
def edit(request, id, ld):
    name_ob = InterimDOC.objects.get(pk=id)
    name_id = name_ob.Ship_InterimDOC_NewShipMainData
    context = {
        "name" : name_id,
    }
    return render(request, 'pages/edit.html', context)


@login_required
def logout(request):
    django_logout(request)
    return  HttpResponseRedirect('/in/login')


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

class DetailView(generic.DetailView):
    """docstring for DetailView"""
    def __init__(self, arg):
        super(DetailView, self).__init__()
        self.arg = arg


# @method_decorator(login_required(login_url="/in/login/"), name='dispatch')
# class CreateCertificateView(CreateView):
#
#
#     def get_form_class(self, **kwargs):
#         """
#         Returns an instance of the form to be used in this view.
#         kwarg from database
#          """
#         return ContextData[self.kwargs['cert_id']]['FormName']
#
#     def get_template_names(self, **kwargs):
#         ShipID = self.request.GET.get('shipid')
#         ModelObject = ContextData[self.kwargs['cert_id']]['ModelName']
#         # if str(ModelObject.objects.filter(CertState='c', ShipMainData__pk=ShipID)) == '<QuerySet []>':
#         #     return 'pages/create-'+ContextData[self.kwargs['cert_id']]['TemplateName']
#         # else:
#         #     return 'pages/active-certificate-error.html'
#         return 'forms/create/create-' + ContextData[self.kwargs['cert_id']]['TemplateName']
#
#     def get_form(self, form_class=None):
#         form = super(CreateCertificateView, self).get_form()
#         return form
#
#     def form_valid(self, form, **kwargs):
#         ShipID = self.request.GET.get('shipid')
#         form.instance.DocAuthor = self.request.user
#         form.instance.ShipMainData = ShipMainData.objects.get(id=ShipID)
#         form.instance.CertState = 'd'
#         return super(CreateCertificateView, self).form_valid(form)


@method_decorator(login_required(login_url="/in/login/"), name='dispatch')
class OwnerIndexView(generic.ListView):
    """docstring for IndexView"""
    template_name = 'pages/owner-view-all.html'
    context_object_name = 'ObjectList'

    def get_queryset(self, **kwargs):
        return ShipOwner.objects.all()


# @method_decorator(login_required(login_url="/in/login/"), name='dispatch')
# class UpdateCertificateView(UpdateView):
#     queryset = None
#
#     def get_form_class(self, **kwargs):
#         """
#         Returns the form class to use in this view
#         """
#         return ContextData[self.kwargs['cert_id']]['FormName']
#
#     def get_queryset(self, **kwargs):
#         """
#         Return the `QuerySet` that will be used to look up the object.
#         Note that this method is called by the default implementation of
#         `get_object` and may not be called if `get_object` is overridden.
#         """
#         ModelObject = ContextData[self.kwargs['cert_id']]['ModelName']
#         return ModelObject.objects.all()
#
#     def get_template_names(self, **kwargs):
#         """
#         Returns a list of template names to be used for the request. Must return
#         a list. May not be called if render_to_response is overridden.
#         """
#         ModelObject = ContextData[self.kwargs['cert_id']]['ModelName']
#         ModelObject = ModelObject.objects.get(pk=self.kwargs['pk'])
#         if ModelObject.CertState=='d':
#             return 'pages/update-'+ContextData[self.kwargs['cert_id']]['TemplateName']
#         else:
#             return 'pages/form-error-update.html'
#
#     def form_valid(self, form):
#         form = self.get_form()
#         form.save()
#         return super(UpdateCertificateView, self).form_valid(form)
#
#     def get_success_url(self):
#         return "../"
#
#     def post(self, request, *args, **kwargs):
#         request.POST = (request.POST.copy())
#         ModelObject = ContextData[self.kwargs['cert_id']]['ModelName']
#         Certificate = ModelObject.objects.get(pk=self.kwargs['pk'])
#         CertFilter = ModelObject.objects.filter(ShipMainData_id=Certificate.ShipMainData.id)
#         State='c'
#         for Certificates in CertFilter: #Check simultaneous confirmation of multiple certificates
#             if Certificates.CertState == "c":
#                 State = 'd'
#         if 'save' in request.POST: #Check before editing or saving confirmed certificates
#             form = self.get_form()
#             if Certificate.CertState != "c":
#                 return super(UpdateCertificateView, self).post(request, *args, **kwargs)
#             else:
#                 return HttpResponseRedirect('../')  # change to redirect
#         if 'confirm' in request.POST:
#             ModelObject.objects.filter(pk=self.kwargs['pk']).update(CertState=State)
#             return HttpResponseRedirect('../')  # change to redirect
#         if 'deactivate' in request.POST:
#             ModelObject.objects.filter(pk=self.kwargs['pk']).update(CertState='x')
#             return HttpResponseRedirect('../') #change to redirect
