from django import forms
from certificates.models import *
from django.forms import extras, ModelForm
# from .models import NewShipMainData, RadioTelephonyCertificate


## Ship Basic
class FormShipFlag(forms.ModelForm):
    class Meta:
        model = ShipFlag
        fields = '__all__'
class FormShipPort(forms.ModelForm):
    class Meta:
        model = ShipPort
        fields = '__all__'
class FormPlaceOfIssue(forms.ModelForm):
    class Meta:
        model = PlaceOfIssue
        fields = '__all__'

##Ship Data
class FormShipOwner(forms.ModelForm):
    class Meta:
        model = ShipOwner
        fields = '__all__'
class FormShipMainData(forms.ModelForm):
    class Meta:
        model = ShipMainData
        fields = '__all__'

##Ship Certificate
class FormCertCSSRTC(forms.ModelForm):
    class Meta:
        model = CertCSSRTC
        fields = '__all__'

class FormCertCSS(forms.ModelForm):
    class Meta:
        model = CertCSS
        fields = '__all__'
class FormCertAFSC(forms.ModelForm):
    class Meta:
        model = CertAFSC
        fields = '__all__'
class FormCertCHMC(forms.ModelForm):
    class Meta:
        model = CertCHMC
        fields = '__all__'
class FormCertCSSC(forms.ModelForm):
    class Meta:
        model = CertCSSC
        fields = '__all__'
class Form(forms.ModelForm):
    class Meta:
        model = ShipOwner
        fields = '__all__'