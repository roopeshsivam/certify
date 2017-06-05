from .models import *
from .forms import *

# ModelTable = {
#             "CertCSSRTC": CertCSSRTC,
#             "CertCSS": CertCSS,
#             "CertCHMC": CertCHMC,
#             "ccssc": CertCSSC,
#             "ccsse": CertCSSE,
#             "CertCSSR": CertCSSR,
#             "CertDOC": CertDOC,
#             "ciapp": CertIAPP,
#             "CertIEE": CertIEE,
#             "CertIOPP": CertIOPP,
#             "CertISPP": CertISPP,
#             "CertISSC": CertISSC,
#             "CertLL": CertLL,
#             "CertIMLC": CertIMLC,
#             "CertSMC": CertSMC,
#             "CertSOPEP": CertSOPEP,
#             "CertSSP": CertSSP,
#             "CertSBA": CertSBA,
#             "CertDG": CertDG,
#             "CertDH": CertDH,
#             "CertFC": CertFC,
#             "RecordAFSC": RecordAFSC,
#         }
#
# FormTable = {
#             "FormCertCSSRTC": FormCertCSSRTC,
#             "FormCertCSS": FormCertCSS,
#             "FormCertCHMC": FormCertCHMC,
#             "ccssc": FormCertCSSC,
#             "ccsse": FormCertCSSE,
#             "FormCertCSSR": FormCertCSSR,
#             "FormCertDOC": FormCertDOC,
#             "ciapp": FormCertIAPP,
#             "FormCertIEE": FormCertIEE,
#             "FormCertIOPP": FormCertIOPP,
#             "FormCertISPP": FormCertISPP,
#             "FormCertISSC": FormCertISSC,
#             "FormCertLL": FormCertLL,
#             "FormCertIMLC": FormCertIMLC,
#             "FormCertSMC": FormCertSMC,
#             "FormCertSOPEP": FormCertSOPEP,
#             "FormCertSSP": FormCertSSP,
#             "FormCertSBA": FormCertSBA,
#             "FormCertDG": FormCertDG,
#             "FormCertDH": FormCertDH,
#             "FormCertFC": FormCertFC,
#             "FormRecordAFSC": FormRecordAFSC,
#         }
#
# TemplateTable = {
#             "ciapp": 'ciapp-certificate-form.html',
# }
ContextShipType = {
            "a": "Passenger Ship",
		    "b": "Passenger HighSpeed Craft",
		    "c": "Cargo HighSpeed Craft",
		    "d": "Bulk Carrier",
		    "e": "Oil Tanker",
		    "f": "Chemical Tanker",
		    "g": "Gas Carrier",
		    "h": "Mobile Offshore Drilling Unit",
		    "i": "Other Cargo Ship"
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

ContextCAFSC = {
    "CertName": "ANTI-FOULING SYSTEM CERTIFICATE",
    "ModelName": TableCAFSC,
    "FormName": FormCAFSC,
    "TemplateName": "cafsc-certificate-form.html",
}

ContextCCHMC = {
    "CertName": "CERTIFICATE OF CLASS HULL & MACHINERY",
    "ModelName": TableCCHMC,
    "FormName": FormCCHMC,
    "TemplateName": "cchmc-certificate-form.html",
}

ContextCCSSC = {
    "CertName": "CARGO SHIP SAFETY CONSTRUCTION CERTIFICATE",
    "ModelName": TableCCSSC,
    "FormName": FormCCSSC,
    "TemplateName": "ccssc-certificate-form.html",
}

ContextCCSSE = {
    "CertName": "CARGO SHIP SAFETY EQUIPMENT CERTIFICATE",
    "ModelName": TableCCSSE,
    "FormName": FormCCSSE,
    "TemplateName": "ccsse-certificate-form.html",
}

ContextCCSSR = {
    "CertName": "CARGO SHIP SAFETY RADIO CERTIFICATE",
    "ModelName": TableCCSSR,
    "FormName": FormCCSSR,
    "TemplateName": "ccssr-certificate-form.html",
}

ContextCCDOC = {
    "CertName": "DOCUMENT OF COMPLIANCE",
    "ModelName": TableCCDOC,
    "FormName": FormCCDOC,
    "TemplateName": "ccdoc-certificate-form.html",
}

ContextCIAPP = {
    "CertName": "INTERNATIONAL AIR POLLUTION PREVENTION CERTIFICATE",
    "ModelName": TableCIAPP,
    "FormName": FormCIAPP,
    "TemplateName": "ciapp-certificate-form.html",
}

ContextCCIEE = {
    "CertName": "INTERNATIONAL ENERGY EFFICIENCY CERTIFICATE",
    "ModelName": TableCCIEE,
    "FormName": FormCCIEE,
    "TemplateName": "cciee-certificate-form.html",
}

ContextCCLLC = {
    "CertName": "INTERNATIONAL LOAD LINE CERTIFICATE (1966)",
    "ModelName": TableCCLLC,
    "FormName": FormCCLLC,
    "TemplateName": "ccllc-certificate-form.html",
}

ContextCIOPP = {
    "CertName": "INTERNATIONAL OIL POLLUTION PREVENTION CERTIFICATE",
    "ModelName": TableCIOPP,
    "FormName": FormCIOPP,
    "TemplateName": "ciopp-certificate-form.html",
}

ContextCISPP = {
    "CertName": "INTERNATIONAL SEWAGE POLLUTION PREVENTION CERTIFICATE",
    "ModelName": TableCISPP,
    "FormName": FormCISPP,
    "TemplateName": "cispp-certificate-form.html",
}

ContextCISSC = {
    "CertName": "INTERNATIONAL SHIP SECURITY CERTIFICATE",
    "ModelName": TableCISSC,
    "FormName": FormCISSC,
    "TemplateName": "cissc-certificate-form.html",
}

ContextCCSMC = {
    "CertName": "SAFETY MANAGEMENT CERTIFICATE",
    "ModelName": TableCCSMC,
    "FormName": FormCCSMC,
    "TemplateName": "ccsmc-certificate-form.html",
}

ContextData = {
    "cafsc": ContextCAFSC,
    "cchmc": ContextCCHMC,
    "ccssc": ContextCCSSC,
    "ccsse": ContextCCSSE,
    "ccssr": ContextCCSSR,
    "ccdoc": ContextCCDOC,
    "ciapp": ContextCIAPP,
    "cciee": ContextCCIEE,
    "ccllc": ContextCCLLC,
    "ciopp": ContextCIOPP,
    "cispp": ContextCISPP,
    "cissc": ContextCISSC,
    "ccsmc": ContextCCSMC,
}