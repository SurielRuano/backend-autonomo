from __future__ import unicode_literals
 
from django.db import models
from django.conf import settings




class trademark(models.Model):
	name = models.CharField(max_length=60)
	logo = models.ImageField(upload_to="assets/trademark", blank=True, null=True)
	
	



	def __str__(self):
		return self.name


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
	



	def __str__(self):
		return self.version


class Vehicle(models.Model):
	
	trademark = models.ForeignKey(trademark)	
	vehicle_version = models.ManyToManyField(Vehicle_version)
	name = models.CharField(max_length=60)
	anio = models.DateField(auto_now=True)
	doors_num = models.IntegerField ()
	cylinders_num = models.IntegerField()
	description_short = models.TextField() 
	description_long = models.TextField()
	img_front = models.ImageField(upload_to="assets", blank=True, null=True)
	img_left = models.ImageField(upload_to="assets", blank=True, null=True)
	img_right = models.ImageField(upload_to= "assets", blank=True, null=True)
	img_back = models.ImageField(upload_to= "assets", blank=True, null=True)
	hp = models.CharField(max_length=50,blank=True, null=True)
	engine = models.CharField(max_length=7, blank=True, null=True)
	price = models.FloatField()




	# def __str__(self):
	# 	return 'Auto {}'.format(self.name)


# Create your models here.


	def __str__(self):
		return self.name




