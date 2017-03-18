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

class CreateCertificateView(CreateView):
    template_name = 'pages/certificate-form.html'
    def get_form_class(self, **kwargs):
        """
        Returns an instance of the form to be used in this view.
        kwarg from database
         """
        FormObject = CertViewManager.objects.get(FieldName=self.kwargs['cert_id'])
        return FormTable[FormObject.FieldName]

    def get_template_names(self, **kwargs):
        ManagerObject = CertViewManager.objects.get(FieldName=self.kwargs['cert_id'])
        ModelObject = ModelTable[ManagerObject.FieldName]
        if str(ModelObject.objects.filter(CertState='b', ShipMainData__pk=self.kwargs['ship_id'])) == '<QuerySet []>':
            return ManagerObject.CreateTemplateName
        else:
            return 'pages/form-error.html'

    def get_form(self, form_class=None):
        form = super(CreateCertificateView, self).get_form()
        return form

    def form_valid(self, form, **kwargs):
        kwargs = super(CreateCertificateView, self).get_form_kwargs()
        ShipData = ShipMainData.objects.get(id=self.kwargs['ship_id'])
        form.instance.DocAuthor = self.request.user
        form.instance.ShipMainData = ShipData
        form.instance.CertState = 'a'
        return super(CreateCertificateView, self).form_valid(form)

@method_decorator(login_required(login_url="/in/login/"), name='dispatch')
class OwnerIndexView(generic.ListView):
    """docstring for IndexView"""
    template_name = 'pages/owner-view-all.html'
    context_object_name = 'ObjectList'
    def get_queryset(self, **kwargs):
        return ShipOwner.objects.all()

@method_decorator(login_required(login_url="/in/login/"), name='dispatch')
class UpdateCertificateView(UpdateView):
    queryset = None
    def get_form_class(self, **kwargs):
        """
        Returns the form class to use in this view
        """
        ManagerObject = CertViewManager.objects.get(FieldName=self.kwargs['cert_id'])
        return FormTable[ManagerObject.FieldName]

    def get_queryset(self, **kwargs):
        """
        Return the `QuerySet` that will be used to look up the object.
        Note that this method is called by the default implementation of
        `get_object` and may not be called if `get_object` is overridden.
        """
        ManagerObject = CertViewManager.objects.get(FieldName=self.kwargs['cert_id'])
        ModelObject = ModelTable[ManagerObject.FieldName]
        return ModelObject.objects.all()

    def get_template_names(self, **kwargs):
        """
        Returns a list of template names to be used for the request. Must return
        a list. May not be called if render_to_response is overridden.
        """
        ManagerObject = CertViewManager.objects.get(FieldName=self.kwargs['cert_id'])
        ModelObject = ModelTable[ManagerObject.FieldName]
        ModelObject = ModelObject.objects.get(pk=self.kwargs['pk'])
        if ModelObject.CertState=='a':
            return ManagerObject.UpdateTemplateName
        else:
            return 'pages/form-error-update.html'

    def form_valid(self, form):
        print(self.request.POST)
        if 'save' in self.request.POST:
            form.instance.CertState = 'a'
        elif 'confirm' in self.request.POST:
            form.instance.CertState = 'b'
        elif 'deactivate' in self.request.POST:
            form.instance.CertState = 'c'
        return super(UpdateCertificateView, self).form_valid(form)

    def post(self, request, **kwargs):
        request.POST = (request.POST.copy())
        ManagerObject = CertViewManager.objects.get(FieldName=self.kwargs['cert_id'])
        ModelObject = ModelTable[ManagerObject.FieldName]
        print(request.POST)
        if 'confirm' in request.POST:
            ModelObject.objects.filter(pk=self.kwargs['pk']).update(CertState='b')
        if 'deactivate' in request.POST:
            ModelObject.objects.filter(pk=self.kwargs['pk']).update(CertState='c')
            return HttpResponseRedirect('/in/own/') #change to redirect