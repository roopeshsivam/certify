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





from .models import *
from .forms import *

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

class CreateCertificateView(CreateView):
    template_name = 'pages/certificate-form.html'
    def get_form_class(self, **kwargs):
        """
        Returns an instance of the form to be used in this view.
        kwarg from database
         """
        FormObject = CertViewManager.objects.get(FieldName=self.kwargs['cert_id'])
        return FormTable[FormObject.FormName]

    def get_template_names(self, **kwargs):
        ManagerObject = CertViewManager.objects.get(FieldName=self.kwargs['cert_id'])
        ModelObject = ManagerObject.ModelName
        ShipData = ShipMainData.objects.get(id=self.kwargs['ship_id'])
        return ManagerObject.TemplateName

    def get_form(self, form_class=None):
        form = super(CreateCertificateView, self).get_form()
        return form

    def form_valid(self, form, **kwargs):
        kwargs = super(CreateCertificateView, self).get_form_kwargs()
        ShipData = ShipMainData.objects.get(id=self.kwargs['ship_id'])
        form.instance.DocAuthor = self.request.user
        form.instance.ShipMainData = ShipData
        return super(CreateCertificateView, self).form_valid(form)
