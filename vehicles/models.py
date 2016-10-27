from __future__ import unicode_literals
 
from django.db import models
from django.conf import settings




class trademark(models.Model):
	name = models.CharField(max_length=60)
	logo = models.ImageField(upload_to="assets/trademark", blank=True, null=True)

	def __str__(self):
		return self.name


class vehicle_color(models.Model):
	color = models.CharField(max_length=60)

	def __str__(self):
		return self.color


class Vehicle_version(models.Model):
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
	

	def __str__(self):
		return self.version


class Vehicle(models.Model):

	trademark = models.ForeignKey(trademark)	
	vehicle_version = models.ManyToManyField(Vehicle_version)
	vehicle_color = models.ManyToManyField(vehicle_color)
	name = models.CharField(max_length=60)
	anio = models.DateField(auto_now=True)	
	description_short = models.TextField()	
	img_front = models.ImageField(upload_to="assets", blank=True, null=True)
	img_left = models.ImageField(upload_to="assets", blank=True, null=True)
	img_right = models.ImageField(upload_to= "assets", blank=True, null=True)
	img_back = models.ImageField(upload_to= "assets", blank=True, null=True)
	

	def __str__(self):
		return self.name



