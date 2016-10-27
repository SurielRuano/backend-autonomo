from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from clients.models import Client
from vehicles.models import Vehicle
# Create your models here.


class VehicleBooking (models.Model):
	id_client = models.ForeignKey(Client, related_name='vehiclebook')
	id_vehicle = models.ForeignKey(Vehicle, related_name='vehiclebook')
	price = models.FloatField()

	class Meta:
		verbose_name = "VehicleBooking"
		verbose_name_plural = "VehicleBookings"

	def __str__(self):
		return self.id_client


class MonthlyPayment(models.Model):
	monthly = models.CharField(max_length=100)
	id_vehiclebooking = models.ForeignKey(VehicleBooking, related_name='monthlypayment')

	class Meta:
		verbose_name = "MonthlyPayment"
		verbose_name_plural = "MonthlyPayments"

	def __str__(self):
		return self.monthly