from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from multiselectfield import MultiSelectField

class UserQueryData(models.Model):
	Enter_First_Name = models.CharField(max_length=30,default='')
	Enter_Last_Name = models.CharField(max_length=30,default='')
	Enter_Email_Id = models.EmailField(max_length=100,default='')
	Enter_Contact_No = models.BigIntegerField(default='')
	VEHICLE = (('Make','Make'),
		('Acura','Acura'),
		('Audi','Audi'),
		('BMW','BMW'),
		('FORD','HONDA'),
		('HONDA','HONDA'),
		('FEEP','FEEP'),
		('LEXUS','LEXUS'),
		('SUZUKI','SUZUKI'))

	YEAR=(('2007','2007'),
		('2008','2008'),
		('2009','2009'),
		('2010','2010'),
		('2011','2011'),
		('2012','2012'),
		('2013','2013'),
		('2014','2014'),
		('2015','2015'),
		('2016','2016'),
		('2017','2017'))

	CAR_MODEL = (('A3 QUATTRO','A3 QUATTRO'),
		('A3 TDI','A3 TDI'),
		('A4','A4'),
		('A4 QUATTRO','A4 QUATTRO'),
		('A5 QUATTRO','A5 QUATTRO'),
		('A6','A6'))
	CAR_SUBMODEL = (('Sports','Sports'),
		('SE','SE'),
		('Limited Edition','Limited Edition'))

	MILEAGE=(('less then 10K','less then 10K'),
		('30K','30K'),
		('40K','40K'),
		('More Than 40K','More Than 40K'))
	SERVICE_TYPE = ((' Oil  Filter Change',' Oil  Filter Change'),
		('Starting  Charging/Battery','Starting  Charging/Battery'),
		('Complete Vehicle Inspection','Complete Vehicle Inspection'),
		(' Tyre Replacement',' Tyre Replacement'),
		(' State Inspection',' State Inspection'),
		('Wiper Blades','Wiper Blades'),
		('Tyre Rotation','Tyre Rotation'),
		('Air Filter  Cabin Air Filter','Air Filter  Cabin Air Filter'),
		('Lighting Bulbs','Lighting &amp; Bulbs'),
		(' Wheel Balance',' Wheel Balance')
		)

	Vehicle_Type= models.CharField(max_length=40, choices=VEHICLE,default='XYZ')
	Year_Old= models.CharField(max_length=40, choices=YEAR,default='XYZ')
	Car_Model_Type = models.CharField(max_length=40,choices=CAR_MODEL,default='XYZ')
	Car_Submodel_Type = models.CharField(max_length=40,choices=CAR_SUBMODEL,default='abc')
	Car_Mileage = models.CharField(max_length=30,choices=MILEAGE,default='20km')
	Service_Request = MultiSelectField(choices=SERVICE_TYPE,default='')


	def __str__(self): 
		return self.Enter_First_Name +" "+self.Enter_Last_Name
	                             
	