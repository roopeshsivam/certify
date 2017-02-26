from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout as django_logout
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView
from django.forms import BaseModelFormSet
from django.views.generic.edit import CreateView



from .models import *
from .forms import *

# from .forms import ShipFormHead

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

@login_required(login_url="/certificates/login/")
def view_all(request):
    return render(request, 'pages/view-all.html')



@login_required(login_url="/certificates/login/")
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
    return  HttpResponseRedirect('/certificates/login')

@method_decorator(login_required(login_url="/certificates/login/"), name='dispatch')
class IndexView(generic.ListView):
    """docstring for IndexView"""
    template_name = 'pages/view-all.html'
    context_object_name = 'ShipNameList'
    def get_queryset(self):
        return ShipMainData.objects.all()

class DetailView(generic.DetailView):
    """docstring for DetailView"""
    def __init__(self, arg):
        super(DetailView, self).__init__()
        self.arg = arg

# class CertificateView(FormView):
#     template_name = 'pages/certificate-form.html'
#     form_class = FormCertCSSRTC
#     success_url = '/thanks/'
#
#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         form.send_email()
#         return super(CertificateView, self).form_valid(form)


# class CertificateView(CreateView):
#     model = ShipMainData
#     fields = '__all__'
#     template_name = 'pages/certificate-form.html'
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super(CertificateView, self).form_valid(form)

class CertificateView(CreateView):
    model = CertCSS
    fields = '__all__'
    template_name = 'pages/certificate-form.html'
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(CertificateView, self).form_valid(form)