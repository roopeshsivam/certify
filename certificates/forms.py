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
    """
    meta Form for certificates
    """
    class Meta:
        fields = '__all__'
        exclude = ('DocAuthor', 'IsActive', 'FieldName', 'ShipMainData', 'IsDraft',)

class FormCertCSSRTC(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = CertCSSRTC
        fields = '__all__'

class FormCertCSS(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = CertCSS
        fields = '__all__'

class FormCertAFSC(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = CertAFSC
        fields = '__all__'

class FormCertCHMC(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = CertCHMC
        fields = '__all__'

class FormCertCSSC(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = CertCSSC
        fields = '__all__'

class FormCertCSSE(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = CertCSSE
        fields = '__all__'

class FormCertCSSR(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = CertCSSR
        fields = '__all__'

class FormCertDOC(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = CertDOC
        fields = '__all__'

class FormCertIAPP(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = CertIAPP
        fields = '__all__'

class FormCertIEE(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = CertIEE
        fields = '__all__'

class FormCertIOPP(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = CertIOPP
        fields = '__all__'

class FormCertISPP(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = CertISPP
        fields = '__all__'

class FormCertISSC(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = CertISSC
        fields = '__all__'

class FormCertLL(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = CertLL
        fields = '__all__'

class FormCertIMLC(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = CertIMLC
        fields = '__all__'

class FormCertSMC(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = CertSMC
        fields = '__all__'

class FormCertSOPEP(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = CertSOPEP
        fields = '__all__'

class FormCertSSP(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = CertSSP
        fields = '__all__'

class FormCertSBA(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = CertSBA
        fields = '__all__'

class FormCertDG(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = CertDG
        fields = '__all__'

class FormCertDH(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = CertDH
        fields = '__all__'

class FormCertFC(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = CertFC
        fields = '__all__'

class FormRecordAFSC(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = RecordAFSC
        fields = '__all__'

FormTable = {
            "FormCertCSSRTC" : FormCertCSSRTC,
            "FormCertCSS" : FormCertCSS,
            "FormCertCHMC" : FormCertCHMC,
            "FormCertCSSC" : FormCertCSSC,
            "FormCertCSSE" : FormCertCSSE,
            "FormCertCSSR" : FormCertCSSR,
            "FormCertDOC" : FormCertDOC,
            "FormCertIAPP" : FormCertIAPP,
            "FormCertIEE" : FormCertIEE,
            "FormCertIOPP" : FormCertIOPP,
            "FormCertISPP" : FormCertISPP,
            "FormCertISSC" : FormCertISSC,
            "FormCertLL" : FormCertLL,
            "FormCertIMLC" : FormCertIMLC,
            "FormCertSMC" : FormCertSMC,
            "FormCertSOPEP" : FormCertSOPEP,
            "FormCertSSP" : FormCertSSP,
            "FormCertSBA" : FormCertSBA,
            "FormCertDG" : FormCertDG,
            "FormCertDH" : FormCertDH,
            "FormCertFC" : FormCertFC,
            "FormRecordAFSC" : FormRecordAFSC,
        }
