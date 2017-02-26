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
class FormCertBase(forms.ModelForm):
    class Meta:
        fields = '__all__'
        exclude = ('DocAuthor', 'IsActive', 'FieldName', 'ShipMainData',)

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

class FormCertCSSC(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = CertCSSC
        fields = '__all__'

class Form(forms.ModelForm):
    class Meta:
        model = ShipOwner
        fields = '__all__'