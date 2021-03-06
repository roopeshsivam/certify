from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User

class CertViewManager(models.Model):
	FieldName = models.CharField(max_length=5, unique=True)
	FormName = models.CharField(max_length=20, null=True)
	ModelName = models.CharField(max_length=20, blank=True)
	CreateTemplateName = models.CharField(max_length=100, blank=True)
	UpdateTemplateName = models.CharField(max_length=100, blank=True)
	DetailTemplateName = models.CharField(max_length=100, blank=True)
	Title = models.CharField(max_length=100, blank=True)
	Description = models.TextField(max_length=100, blank=True)
	def __str__(self):
		return self.FieldName

class ShipFlag(models.Model):
	FlagName = models.CharField(max_length=200)
	def __str__(self):
		return self.FlagName

class ShipPort(models.Model):
	PortName = models.CharField(max_length=200)
	def __str__(self):
		return self.PortName

class PlaceOfIssue(models.Model):
	Place = models.CharField(max_length=200)
	def __str__(self):
		return self.Place

class AbstractData(models.Model):
	DocCreated = models.DateTimeField(auto_now=False, auto_now_add=True)
	DocLastUpdated = models.DateTimeField(auto_now=True, auto_now_add=False)
	DocAuthor = models.ForeignKey(User, null=True, blank=True)
	class Meta:
		abstract = True

class CertificateManage(AbstractData):
	CertChoice = (
		('a', 'Interim'),
		('b', 'Full Term'),
	)
	StateChoice = (
		('d', 'Draft'),
		('c', 'Confirmed'),
		('x', 'DeActivated')
	)
	CertType = models.CharField(max_length=1, choices=CertChoice)
	CertState = models.CharField(max_length=1, choices=StateChoice)
	ShipMainData = models.ForeignKey('ShipMainData', on_delete=models.PROTECT)
	PlaceOfIssues = models.ForeignKey('PlaceOfIssue', on_delete=models.PROTECT)
	DateCompletion = models.DateField()
	DateIssued = models.DateField()
	DateValidity = models.DateField()
	class Meta:
		abstract = True
	def active(self):
		if self.IsActive:
			active = ''
		else:
			active = 'disabled'
		return active
	def get_absolute_url(self):
		return "../%s/" %(self.pk)

class ShipOwner(AbstractData):
	Name = models.CharField(max_length=200)
	IDNumber = models.PositiveIntegerField(unique=True, validators=[MaxValueValidator(9999999999), MinValueValidator(1)],)
	CompanyName = models.CharField(max_length=200)
	CompanyAddress = models.TextField()
	Phone = models.CharField(max_length=200)
	Email = models.CharField(max_length=200)
	def __str__(self):
		return str(self.IDNumber)
	def get_absolute_url(self):
		return "/in/own/%s/" %(self.pk)

class ShipMainData(AbstractData):
	ShipType = (
		('a', 'Passenger Ship'),
		('b', 'Passenger HighSpeed Craft'),
		('c', 'Cargo HighSpeed Craft'),
		('d', 'Bulk Carrier'),
		('e', 'Oil Tanker'),
		('f', 'Chemical Tanker'),
		('g', 'Gas Carrier'),
		('h', 'Mobile Offshore Drilling Unit'),
		('i', 'Other Cargo Ship')
	)
	Name = models.CharField(max_length=200)
	IMONumber = models.PositiveIntegerField(unique=True, validators=[MaxValueValidator(9999999999), MinValueValidator(1)],)
	DNL = models.CharField(max_length=200)
	OldName = models.CharField(max_length=200)
	Type = models.CharField(max_length=1, choices=ShipType)
	Length = models.PositiveIntegerField(validators=[MaxValueValidator(9999999), MinValueValidator(1)],)
	GrossTonnage = models.PositiveIntegerField(validators=[MaxValueValidator(9999999), MinValueValidator(1)],)
	NetTonnage = models.PositiveIntegerField(validators=[MaxValueValidator(9999999), MinValueValidator(1)],)
	BuiltYear = models.PositiveIntegerField(validators=[MaxValueValidator(2099), MinValueValidator(1900)],)
	DeliveryDate = models.PositiveIntegerField(validators=[MaxValueValidator(2099), MinValueValidator(1900)],)
	NumberOfPerson = models.PositiveIntegerField(validators=[MaxValueValidator(999), MinValueValidator(1)],)
	FLAG = models.ForeignKey('ShipFlag', on_delete=models.PROTECT)
	PortOfRegistry = models.ForeignKey('ShipPort', on_delete=models.PROTECT)
	Owner = models.ForeignKey('ShipOwner', on_delete=models.PROTECT)
	BuilderName = models.CharField(max_length=200)
	BuilderPlace = models.CharField(max_length=200)
	def __str__(self):
		return self.Name

	def get_absolute_url(self):
		return "/in/ship/%s/" %(self.pk)

	def get_certificate(self):
		return self._default_manager.filter(ShipMainData=self)

	def natural_key(self):
		return self.my_natural_key

# class CertCSSRTC(CertificateManage):
# 	FieldName = models.CharField(max_length=5, default = "cssrt")
# 	Row001_Req = models.BooleanField()
# 	Row001_Ins = models.BooleanField()
# 	Row002_Req = models.BooleanField()
# 	Row002_Ins = models.BooleanField()
# 	Row003_Req = models.BooleanField()
# 	Row003_Ins = models.BooleanField()
# 	Row004_Req = models.BooleanField()
# 	Row004_Ins = models.BooleanField()
# 	def __str__(self):
# 		return str(self.ShipMainData.IMONumber)
#
# class CertCSS(CertificateManage):
# 	FieldName = models.CharField(max_length=5, default = "ctcss")
# 	AuthorizedMiles = models.PositiveIntegerField(validators=[MaxValueValidator(999999), MinValueValidator(1)],)
# 	LifeSavings_Total = models.PositiveIntegerField(validators=[MaxValueValidator(9999), MinValueValidator(1)],)
# 	LifeBoats_Number = models.PositiveIntegerField(validators=[MaxValueValidator(9999), MinValueValidator(1)],)
# 	LifeBoats_Person = models.PositiveIntegerField(validators=[MaxValueValidator(9999), MinValueValidator(1)],)
# 	MotorBoatsNumber = models.PositiveIntegerField(validators=[MaxValueValidator(9999), MinValueValidator(1)],)
# 	MotorBoatsPerson = models.PositiveIntegerField(validators=[MaxValueValidator(9999), MinValueValidator(1)],)
# 	LifeRaftDevice_Req = models.BooleanField()
# 	LifeRaftNumber = models.PositiveIntegerField(validators=[MaxValueValidator(9999), MinValueValidator(1)],)
# 	LifebuoysNumber = models.PositiveIntegerField(validators=[MaxValueValidator(9999), MinValueValidator(1)],)
# 	LifejacketsNumber = models.PositiveIntegerField(validators=[MaxValueValidator(9999), MinValueValidator(1)],)
# 	def __str__(self):
# 		return str(self.ShipMainData.IMONumber)
#
#
# class CertAFSC(CertificateManage):
# 	FieldName = models.CharField(max_length=5, default = "ctafs")
# 	PreviousIssued = models.DateField()
# 	AppliedConstruction = models.BooleanField()
# 	RemovedBy = models.CharField(max_length=200, default = "--")
# 	RemovedDate = models.DateField()
# 	RemovedPreviously_Req = models.BooleanField()
# 	CoveredBy = models.CharField(max_length=200)
# 	CoveredDate = models.DateField()
# 	CoveredCheck_Req = models.BooleanField()
# 	Prior = models.CharField(max_length=200)
# 	PriorRemovedCovered = models.CharField(max_length=200)
# 	PriorCheck_Req = models.BooleanField()
# 	def __str__(self):
# 		return str(self.ShipMainData.IMONumber)
#
# class CertCHMC(CertificateManage):
# 	FieldName = models.CharField(max_length=5, default = "ctchm")
# 	BuilderName = models.CharField(max_length=200)
# 	BuilderPlace = models.CharField(max_length=200)
#
# 	def __str__(self):
# 		return str(self.ShipMainData.IMONumber)
#
# class CertCSSC(CertificateManage):
# 	FieldName = models.CharField(max_length=5, default = "ccssc")
# 	KeelLaidDate = models.DateField() #Also for CSSR
# 	AlterationDate = models.DateField()
# 	LastInspectionDate_001 = models.DateField()
# 	LastInspectionDate_002 = models.DateField()
# 	def __str__(self):
# 		return str(self.ShipMainData.IMONumber)
#
# class CertCSSE(CertificateManage):
# 	FieldName = models.CharField(max_length=5, default = "ccsse")
# 	def __str__(self):
# 		return str(self.ShipMainData.IMONumber)
# 	class Meta:
# 		default_related_name = 'interimcsse'
# 	def get_certificate(self):
# 		return self._default_manager.filter(ShipMainData=self)
#
# class CertCSSR(CertificateManage):
# 	FieldName = models.CharField(max_length=5, default = "ccssr")
# 	AreaA1 = models.BooleanField()
# 	AreaA2 = models.BooleanField()
# 	AreaA3 = models.BooleanField()
# 	AreaA4 = models.BooleanField()
# 	AreaA5 = models.BooleanField()
# 	def __str__(self):
# 		return str(self.ShipMainData.IMONumber)
#
# class CertDOC(CertificateManage):
# 	FieldName = models.CharField(max_length=5, default = "ctdoc")
# 	def __str__(self):
# 		return str(self.ShipMainData.IMONumber)
#
# class CertIAPP(CertificateManage):
# 	FieldName = models.CharField(max_length=5, default = "ciapp")
# 	def __str__(self):
# 		return str(self.ShipMainData.IMONumber)
#
# class CertIEE(CertificateManage):
# 	FieldName = models.CharField(max_length=5, default = "cieee")
# 	def __str__(self):
# 		return str(self.ShipMainData.IMONumber)
#
# class CertIOPP(CertificateManage):
# 	FieldName = models.CharField(max_length=5, default = "ciopp")
# 	def __str__(self):
# 		return str(self.ShipMainData.IMONumber)
#
# class CertISPP(CertificateManage):
# 	FieldName = models.CharField(max_length=5, default = "cispp")
# 	SewagePlant = models.CharField(max_length=200)
# 	SewagePlantManufacture = models.CharField(max_length=200)
# 	ComminuterType = models.CharField(max_length=200)
# 	ComminuterManufacture = models.CharField(max_length=200)
# 	TankHoldCapacity = models.CharField(max_length=200)
# 	TankLocation = models.CharField(max_length=200)
# 	def __str__(self):
# 		return str(self.ShipMainData.IMONumber)
#
# class CertISSC(CertificateManage):
# 	FieldName = models.CharField(max_length=5, default = "cissc")
# 	YesNo = (
# 		('a', 'Yes'),
# 		('b', 'No')
# 	)
# 	IsSubsequentCertificate = models.CharField(max_length=1, choices=YesNo)
# 	InitialIssuedDate = models.DateField()
# 	def __str__(self):
# 		return str(self.ShipMainData.IMONumber)
#
# class CertLL(CertificateManage):
# 	FieldName = models.CharField(max_length=5, default = "cssll")
# 	FreeBoard = (
# 		('a', 'A New Ship'),
# 		('b', 'An Existing Ship')
# 	)
# 	TypeOfShip = (
# 		('a', 'Type A'),
# 		('b', 'Type B'),
# 		('c', 'With reduced'),
# 		('d', 'increased freeboard')
# 	)
# 	FreeboardAssigned = models.CharField(max_length=1, choices=FreeBoard)
# 	TypeOfShip = models.CharField(max_length=1, choices=TypeOfShip)
# 	DeckTropicalMM = models.CharField(max_length=8, default="-")
# 	DeckSummerMM = models.CharField(max_length=8, default="-")
# 	DeckWinterMM = models.CharField(max_length=8, default="-")
# 	DeckWinterNorthMM = models.CharField(max_length=8, default="-")
# 	DeckTimTropicalMM = models.CharField(max_length=8, default="-")
# 	DeckTimSummerMM = models.CharField(max_length=8, default="-")
# 	DeckTimWinterMM = models.CharField(max_length=8, default="-")
# 	DeckTimWinterNorthMM = models.CharField(max_length=8, default="-")
# 	LoadTropicalMM = models.CharField(max_length=8, default="-")
# 	LoadSummerMM = models.CharField(max_length=8, default="-")
# 	LoadWinterMM = models.CharField(max_length=8, default="-")
# 	LoadWinterNorthMM = models.CharField(max_length=8, default="-")
# 	LoadTimTropicalMM = models.CharField(max_length=8, default="-")
# 	LoadTimSummerMM = models.CharField(max_length=8, default="-")
# 	LoadTimWinterMM = models.CharField(max_length=8, default="-")
# 	LoadTimWinterNorthMM = models.CharField(max_length=8, default="-")
# 	Allowance_FreshWaterMM = models.CharField(max_length=8, default="-")
# 	Allowance_FreeboardMM = models.CharField(max_length=8, default="-")
# 	Deck_FreeboardMM = models.CharField(max_length=8, default="-")
# 	def __str__(self):
# 		return str(self.ShipMainData.IMONumber)
#
# class CertIMLC(CertificateManage):
# 	FieldName = models.CharField(max_length=5, default = "cimlc")
# 	def __str__(self):
# 		return str(self.ShipMainData.IMONumber)
#
# class CertSMC(CertificateManage):
# 	FieldName = models.CharField(max_length=5, default = "cssmc")
# 	def __str__(self):
# 		return str(self.ShipMainData.IMONumber)
#
# class CertSOPEP(CertificateManage):
# 	FieldName = models.CharField(max_length=5, default = "sopep")
# 	def __str__(self):
# 		return str(self.ShipMainData.IMONumber)
#
# class CertSSP(CertificateManage):
# 	FieldName = models.CharField(max_length=5, default = "ctssp")
# 	def __str__(self):
# 		return str(self.ShipMainData.IMONumber)
#
# class CertSBA(CertificateManage):
# 	FieldName = models.CharField(max_length=5, default = "ctsba")
# 	def __str__(self):
# 		return str(self.ShipMainData.IMONumber)
#
# class CertDG(CertificateManage):
# 	FieldName = models.CharField(max_length=5, default = "crtdg")
# 	Manufacturer = models.CharField(max_length=200)
# 	Model = models.CharField(max_length=200)
# 	def __str__(self):
# 		return str(self.ShipMainData.IMONumber)
#
# class CertDH(CertificateManage):
# 	FieldName = models.CharField(max_length=5, default = "crtdh")
# 	Manufacturer = models.CharField(max_length=200)
# 	Model = models.CharField(max_length=200)
# 	def __str__(self):
# 		return str(self.ShipMainData.IMONumber)
#
# class CertFC(CertificateManage):
# 	FieldName = models.CharField(max_length=5, default = "crtfc")
# 	def __str__(self):
# 		return str(self.ShipMainData.IMONumber)
#
# class RecordAFSC(CertificateManage):
# 	FieldName = models.CharField(max_length=5, default = "ctafsc")
# 	AppliedUsed = models.CharField(max_length=300)
# 	AppliedDate = models.DateField()
# 	AppliedCompany = models.CharField(max_length=200)
# 	AppliedManufacturer = models.CharField(max_length=200)
# 	AppliedColor = models.TextField()
# 	AppliedIngredients = models.TextField()
# 	SealerCoatType = models.TextField()
# 	SealerCoatColor = models.TextField()
# 	SealerCoatDate = models.DateField()
# 	def __str__(self):
# 		return str(self.ShipMainData.IMONumber)
#
#




class TableCAFSC(CertificateManage):
	PreviousIssued = models.DateField()
	AppliedConstruction = models.BooleanField()
	RemovedBy = models.CharField(max_length=200, default = "--")
	RemovedDate = models.DateField()
	RemovedPreviously_Req = models.BooleanField()
	CoveredBy = models.CharField(max_length=200)
	CoveredDate = models.DateField()
	CoveredCheck_Req = models.BooleanField()
	Prior = models.CharField(max_length=200)
	PriorRemovedCovered = models.CharField(max_length=200)
	PriorCheck_Req = models.BooleanField()
	def __str__(self):
		return str(self.ShipMainData.IMONumber)

class TableCCHMC(CertificateManage):
	BuilderName = models.CharField(max_length=200)
	BuilderPlace = models.CharField(max_length=200)
	def __str__(self):
		return str(self.ShipMainData.IMONumber)

class TableCCSSC(CertificateManage):
	KeelLaidDate = models.DateField() #Also for CSSR
	AlterationDate = models.DateField()
	LastInspectionDate_001 = models.DateField()
	LastInspectionDate_002 = models.DateField()
	def __str__(self):
		return str(self.ShipMainData.IMONumber)

class TableCCSSE(CertificateManage):
	def __str__(self):
		return str(self.ShipMainData.IMONumber)
	class Meta:
		default_related_name = 'interimcsse'
	def get_certificate(self):
		return self._default_manager.filter(ShipMainData=self)

class TableCCSSR(CertificateManage):
	AreaA1 = models.BooleanField()
	AreaA2 = models.BooleanField()
	AreaA3 = models.BooleanField()
	AreaA4 = models.BooleanField()
	AreaA5 = models.BooleanField()
	def __str__(self):
		return str(self.ShipMainData.IMONumber)

class TableCCDOC(CertificateManage):
	def __str__(self):
		return str(self.ShipMainData.IMONumber)

class TableCIAPP(CertificateManage):
	def __str__(self):
		return str(self.ShipMainData.IMONumber)

class TableCCIEE(CertificateManage):
	def __str__(self):
		return str(self.ShipMainData.IMONumber)

class TableCIOPP(CertificateManage):
	def __str__(self):
		return str(self.ShipMainData.IMONumber)

class TableCISPP(CertificateManage):
	SewagePlant = models.CharField(max_length=200)
	SewagePlantManufacture = models.CharField(max_length=200)
	ComminuterType = models.CharField(max_length=200)
	ComminuterManufacture = models.CharField(max_length=200)
	TankHoldCapacity = models.CharField(max_length=200)
	TankLocation = models.CharField(max_length=200)
	def __str__(self):
		return str(self.ShipMainData.IMONumber)

class TableCISSC(CertificateManage):
	YesNo = (
		('a', 'Yes'),
		('b', 'No')
	)
	IsSubsequentCertificate = models.CharField(max_length=1, choices=YesNo)
	InitialIssuedDate = models.DateField()
	def __str__(self):
		return str(self.ShipMainData.IMONumber)

class TableCCLLC(CertificateManage):
	FreeBoard = (
		('a', 'A New Ship'),
		('b', 'An Existing Ship')
	)
	TypeOfShip = (
		('a', 'Type A'),
		('b', 'Type B'),
		('c', 'With reduced'),
		('d', 'increased freeboard')
	)
	FreeboardAssigned = models.CharField(max_length=1, choices=FreeBoard)
	TypeOfShip = models.CharField(max_length=1, choices=TypeOfShip)
	DeckTropicalMM = models.CharField(max_length=8, default="-")
	DeckSummerMM = models.CharField(max_length=8, default="-")
	DeckWinterMM = models.CharField(max_length=8, default="-")
	DeckWinterNorthMM = models.CharField(max_length=8, default="-")
	DeckTimTropicalMM = models.CharField(max_length=8, default="-")
	DeckTimSummerMM = models.CharField(max_length=8, default="-")
	DeckTimWinterMM = models.CharField(max_length=8, default="-")
	DeckTimWinterNorthMM = models.CharField(max_length=8, default="-")
	LoadTropicalMM = models.CharField(max_length=8, default="-")
	LoadSummerMM = models.CharField(max_length=8, default="-")
	LoadWinterMM = models.CharField(max_length=8, default="-")
	LoadWinterNorthMM = models.CharField(max_length=8, default="-")
	LoadTimTropicalMM = models.CharField(max_length=8, default="-")
	LoadTimSummerMM = models.CharField(max_length=8, default="-")
	LoadTimWinterMM = models.CharField(max_length=8, default="-")
	LoadTimWinterNorthMM = models.CharField(max_length=8, default="-")
	Allowance_FreshWaterMM = models.CharField(max_length=8, default="-")
	Allowance_FreeboardMM = models.CharField(max_length=8, default="-")
	Deck_FreeboardMM = models.CharField(max_length=8, default="-")
	def __str__(self):
		return str(self.ShipMainData.IMONumber)

class TableCCSMC(CertificateManage):
	def __str__(self):
		return str(self.ShipMainData.IMONumber)
