from .models import *
from .forms import *
ModelTable = {
            "CertCSSRTC": CertCSSRTC,
            "CertCSS": CertCSS,
            "CertCHMC": CertCHMC,
            "ccssc": CertCSSC,
            "ccsse": CertCSSE,
            "CertCSSR": CertCSSR,
            "CertDOC": CertDOC,
            "ciapp": CertIAPP,
            "CertIEE": CertIEE,
            "CertIOPP": CertIOPP,
            "CertISPP": CertISPP,
            "CertISSC": CertISSC,
            "CertLL": CertLL,
            "CertIMLC": CertIMLC,
            "CertSMC": CertSMC,
            "CertSOPEP": CertSOPEP,
            "CertSSP": CertSSP,
            "CertSBA": CertSBA,
            "CertDG": CertDG,
            "CertDH": CertDH,
            "CertFC": CertFC,
            "RecordAFSC": RecordAFSC,
        }
FormTable = {
            "FormCertCSSRTC": FormCertCSSRTC,
            "FormCertCSS": FormCertCSS,
            "FormCertCHMC": FormCertCHMC,
            "ccssc": FormCertCSSC,
            "ccsse": FormCertCSSE,
            "FormCertCSSR": FormCertCSSR,
            "FormCertDOC": FormCertDOC,
            "ciapp": FormCertIAPP,
            "FormCertIEE": FormCertIEE,
            "FormCertIOPP": FormCertIOPP,
            "FormCertISPP": FormCertISPP,
            "FormCertISSC": FormCertISSC,
            "FormCertLL": FormCertLL,
            "FormCertIMLC": FormCertIMLC,
            "FormCertSMC": FormCertSMC,
            "FormCertSOPEP": FormCertSOPEP,
            "FormCertSSP": FormCertSSP,
            "FormCertSBA": FormCertSBA,
            "FormCertDG": FormCertDG,
            "FormCertDH": FormCertDH,
            "FormCertFC": FormCertFC,
            "FormRecordAFSC": FormRecordAFSC,
        }
TemplateTable = {
            "ccssc": FormCertCSSC,
            "ccsse": 'ccsse-certificate-form.html',
            "ciapp": 'ciapp-certificate-form.html',

}
CertState = {
            "c": "Confirmed",
            "d": "Draft",
            "x": "Deactivated"
}
CertType = {
            "a": "Interim",
            "b": "Full Term",
}
CertName = {
            "ciapp": "INTERNATIONAL AIR POLLUTION PREVENTION CERTIFICATE (IAPP)",
}