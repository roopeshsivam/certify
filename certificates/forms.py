from django import forms
from certificates.models import *
from django.forms import extras, ModelForm


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

class FormShipOwner(forms.ModelForm):
    class Meta:
        model = ShipOwner
        fields = '__all__'
class FormShipMainData(forms.ModelForm):
    class Meta:
        model = ShipMainData
        fields = '__all__'

class FormCertBase(forms.ModelForm):
    """
    meta Form for certificates
    """
    class Meta:
        fields = '__all__'
        exclude = ('DocAuthor', 'IsActive', 'FieldName', 'ShipMainData', 'IsDraft', 'CertState', )

class FormCAFSC(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = TableCAFSC
        fields = '__all__'

class FormCCHMC(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = TableCCHMC
        fields = '__all__'

class FormCCSSC(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = TableCCSSC
        fields = '__all__'

class FormCCSSE(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = TableCCSSE
        fields = '__all__'

class FormCCSSR(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = TableCCSSR
        fields = '__all__'

class FormCCDOC(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = TableCCDOC
        fields = '__all__'

class FormCIAPP(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = TableCIAPP
        fields = '__all__'

class FormCCIEE(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = TableCCIEE
        fields = '__all__'

class FormCCLLC(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = TableCCLLC
        fields = '__all__'

class FormCIOPP(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = TableCIOPP
        fields = '__all__'

class FormCISPP(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = TableCISPP
        fields = '__all__'

class FormCISSC(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = TableCISSC
        fields = '__all__'

class FormCCSMC(FormCertBase):
    class Meta(FormCertBase.Meta):
        model = TableCCSMC
        fields = '__all__'
