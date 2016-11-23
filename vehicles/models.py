from __future__ import unicode_literals 
from django.db import models
from django.conf import settings



class trademark(models.Model):
	name = models.CharField(max_length=60)
	logo = models.ImageField(upload_to="assets/trademark", blank=True, null=True)

	def __str__(self):
		return self.name


class Vehicle(models.Model):

	STATUS_CHOICES = (('unpublished','Unpublished'),('published','Published'),)

	trademark = models.ForeignKey(trademark)	
	name = models.CharField(max_length=60)
	anio = models.DateField(auto_now=True)	
	description_short = models.TextField()	
	img_front = models.ImageField(upload_to="assets/vehicles/%Y/%m/%d/", blank=True, null=True)
	img_left = models.ImageField(upload_to="assets/vehicles/%Y/%m/%d/", blank=True, null=True)
	img_right = models.ImageField(upload_to= "assets/vehicles/%Y/%m/%d/", blank=True, null=True)
	img_back = models.ImageField(upload_to= "assets/vehicles/%Y/%m/%d/", blank=True, null=True)
	publication_status = models.CharField(max_length= 11, choices=STATUS_CHOICES, default = 'unpublished')
	v_slug = models.SlugField(max_length=250,unique_for_date='publish', null=True, blank=True)

	def __str__(self):
		return self.name


class Vehicle_version(models.Model):

	vehicle = models.ForeignKey(Vehicle, related_name='version')	
	version = models.CharField(max_length=60)	
	transmission = models.CharField(max_length=7, blank=True, null=True)
	gas_type = models.CharField(max_length=7, blank=True, null=True)	
	hydraulic_power_steering = models.BooleanField(default=False)	
	hp = models.CharField(max_length=50,blank=True, null=True)
	engine = models.CharField(max_length=7, blank=True, null=True)
	price = models.FloatField()
	doors_num = models.IntegerField ()
	cylinders_num = models.IntegerField()
	description_long = models.TextField()

	#security
	airbag = models.BooleanField(default=False)
	brake_abs = models.BooleanField(default=False)
	alarm = models.BooleanField(default=False)
	stability_control = models.BooleanField(default=False)
	foglamps = models.BooleanField(default=False)
	#confort
	electric_glasses = models.BooleanField(default=False)
	electric_door_locks = models.BooleanField(default=False)
	leather_seats = models.BooleanField(default=False)
	sport_wheels = models.BooleanField(default=False)
	air_conditioner = models.BooleanField(default=False)
	electric_mirrors = models.BooleanField(default=False)
	rear_wiper = models.BooleanField(default=False)
	xenon_lights = models.BooleanField(default=False)
	sunroof = models.BooleanField(default=False)
	autoestereo = models.BooleanField(default=False)	
	bluetooth = models.BooleanField(default=False)
	cd = models.BooleanField(default=False)
	dvd = models.BooleanField(default=False)
	usb = models.BooleanField(default=False)
	mp3 = models.BooleanField(default=False)
	radio = models.BooleanField(default=False)

	img_v1 = models.ImageField(upload_to="assets/vehicles/version",blank=True,null=True)
	img_v2 = models.ImageField(upload_to="assets/vehicles/version",blank=True,null=True)
	img_v3 = models.ImageField(upload_to="assets/vehicles/version",blank=True,null=True)
	img_v4 = models.ImageField(upload_to="assets/vehicles/version",blank=True,null=True)
	


	def fee_mounth_48(self):

		fee_48 = (((self.price)/48)*(1.08))*(1.03)

		return fee_48

	def fee_mounth_60(self):

		fee_60 = (((self.price)/60)*(1.08))*(1.03)

		return fee_60

	def fee_inscription(self):

		fee_ins = (self.price)*(0.01)

		return fee_ins




	fee48 = property(fee_mounth_48)
	fee60 = property(fee_mounth_60)
	
	fee_ins = property(fee_inscription)
	

	def __str__(self):
		return self.version






