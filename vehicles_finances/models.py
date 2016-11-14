from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from clients.models import Client
from vehicles.models import Vehicle
# Create your models here.

class StockExchange(models.Model):
	name = models.CharField (max_length=200)
	description = models.TextField()
	maximum_number_customers = models.IntegerField()
	##Tipo de mensualidad 60 o 40 mensualidades
	monthly = models.IntegerField()

	class Meta:
		verbose_name = "StockExchange"
		verbose_name_plural = "StockExchanges"

	def __str__(self):
		return self.name

class VehicleBooking (models.Model):
	BOOL_CHOICES = ((True, 'Adjudicado'),(False, 'No Adjudicado'))
	BOOL_CHOICES2 = ((True, 'Activo'), (False, 'Finalizado'))
	id_client = models.ForeignKey(Client, related_name='vehiclebook')
	id_vehicle = models.ForeignKey(Vehicle, related_name='vehiclebook')
	id_stock = models.ForeignKey(StockExchange, related_name='vehiclebook')
	price = models.FloatField()
	deadline = models.DateField()
	adjudication = models.BooleanField(choices=BOOL_CHOICES, default=False)
	##Camos de contrato
	reference_agreement = models.CharField(max_length=50)
	zone = models.CharField(max_length=50)
	observations = models.TextField()
	date = models.DateField()
	status = models.BooleanField()



	class Meta:
		verbose_name = "VehicleBooking"
		verbose_name_plural = "VehicleBookings"

	# def __str__(self):
	# 	return self.id_client

class DetailPayment (models.Model):
	id_vehiclebooking = models.ForeignKey(VehicleBooking, related_name='detailpayment')
	concept = models.CharField(max_length=250)
	#cantidad
	amount = models.FloatField()
	observations = models.TextField()
	date_payment = models.DateField()
	reference_payment = models.IntegerField()

	class Meta:
		verbose_name = "DetailPayment"
		verbose_name_plural = "DetailPayments"

	# def __str__(self):
	# 	return self.id_vehiclebooking


class SettingsFinantial(models.Model):
	update_factor = models.FloatField()
	administration_fee = models.FloatField()
	inscription_fee = models.FloatField()

	class Meta:
		verbose_name = "SettingsFinantial"
		verbose_name_plural = "SettingsFinantials"

		# def __str__(self):
		# 	return (self.update_factor, self.administration_fee)


# class MonthlyPayment(models.Model):
# 	monthly = models.CharField(max_length=100)
# 	id_vehiclebooking = models.ForeignKey(VehicleBooking, related_name='monthlypayment')

# 	class Meta:
# 		verbose_name = "MonthlyPayment"
# 		verbose_name_plural = "MonthlyPayments"

# 	def __str__(self):
# 		return self.monthly
