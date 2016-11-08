from __future__ import unicode_literals 
from django.db import models
from django.conf import settings



class trademark(models.Model):
	name = models.CharField(max_length=60)
	logo = models.ImageField(upload_to="assets/trademark", blank=True, null=True)

	def __str__(self):
		return self.name





class Vehicle(models.Model):

	trademark = models.ForeignKey(trademark)	
	name = models.CharField(max_length=60)
	anio = models.DateField(auto_now=True)	
	description_short = models.TextField()	
	img_front = models.ImageField(upload_to="assets/vehicles", blank=True, null=True)
	img_left = models.ImageField(upload_to="assets/vehicles", blank=True, null=True)
	img_right = models.ImageField(upload_to= "assets/vehicles", blank=True, null=True)
	img_back = models.ImageField(upload_to= "assets/vehicles", blank=True, null=True)
	

	def __str__(self):
		return self.name




class Vehicle_version(models.Model):
	vehicle = models.ForeignKey(Vehicle, related_name='version')	
	version = models.CharField(max_length=60)
	airbag = models.BooleanField(default=False)
	sunroof = models.BooleanField(default=False)
	bluetooth = models.BooleanField(default=False)
	hydraulic_power_steering = models.BooleanField(default=False)
	autoestereo = models.BooleanField(default=False)
	electric_glasses = models.BooleanField(default=False)
	electric_door_locks = models.BooleanField(default=False)
	leather_seats = models.BooleanField(default=False)
	sport_wheels = models.BooleanField(default=False)
	hp = models.CharField(max_length=50,blank=True, null=True)
	engine = models.CharField(max_length=7, blank=True, null=True)
	price = models.FloatField()
	description_long = models.TextField()
	doors_num = models.IntegerField ()
	cylinders_num = models.IntegerField()
	



	def fee_mounth_48(self):

		fee_48 = (((self.price)/48)*(1.08))*(1.03)

		return fee_48

	def fee_mounth_60(self):

		fee_60 = (((self.price)/60)*(1.08))*(1.03)

		return fee_60




	fee48 = property(fee_mounth_48)
	fee60 = property(fee_mounth_60)
	

	def __str__(self):
		return self.version






