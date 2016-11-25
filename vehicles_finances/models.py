from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from clients.models import Client
from vehicles.models import Vehicle, Vehicle_version
import uuid
# Create your models here.

class StockExchange(models.Model):
	
	##Tipo de mensualidad 60 o 40 mensualidades
	description = models.TextField()	
	monthly = models.IntegerField()

	class Meta:
		verbose_name = "StockExchange"
		verbose_name_plural = "StockExchanges"

	def __str__(self):
		return str(self.monthly)

class groups_stockExchange(models.Model):
	stockexchange = models.ForeignKey(StockExchange, related_name= 'groups_stockExchange')
	unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	maximum_number_customers = models.IntegerField()
	group_description = models.TextField()

	def __str__(self):
		return str(self.unique_id)








class SettingsFinantial(models.Model):
	update_factor = models.FloatField()
	administration_fee = models.FloatField()
	inscription_fee = models.FloatField()

	class Meta:
		verbose_name = "SettingsFinantial"
		verbose_name_plural = "SettingsFinantials"

		# def __str__(self):
		# 	return (self.update_factor, self.administration_fee)

class  Payment_methods(models.Model):


	name =  models.CharField(max_length=100)



	def __str__(self):

		return self.name






class Agreement(models.Model):

	unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)	
	BOOL_CHOICES = ((True, 'Activo'), (False, 'Finalizado'))	
	zone = models.CharField(max_length=50)
	observations = models.TextField()
	date = models.DateField()
	status = models.BooleanField()
	BOOL_CHOICES2 = ((True, 'Adjudicado'),(False, 'No Adjudicado'))	
	id_client = models.ForeignKey(Client, related_name='agreement')
	id_vehicle_version = models.ForeignKey(Vehicle_version, related_name='agreement')
	groups_stockexchange = models.ForeignKey(groups_stockExchange, related_name='agreement')
	vehicle_price = models.FloatField()
	payment_deadline = models.DateField()
	adjudication = models.BooleanField(choices=BOOL_CHOICES2, default=False)
	##Camos de contrato	

	def __str__(self):

		return str(self.unique_id)


class DetailPayment (models.Model):
	
	agreement = models.ForeignKey(Agreement, related_name='detail_payment' )
	concept = models.CharField(max_length=250)
	payment_reference = models.CharField(max_length=400, null= True, blank = True)
	amount = models.FloatField()
	observations = models.TextField()
	date_payment = models.DateField()


	class Meta:
		verbose_name = "DetailPayment"
		verbose_name_plural = "DetailPayments"

	def __str__(self):
		return self.concept




# class MonthlyPayment(models.Model):
# 	monthly = models.CharField(max_length=100)
# 	id_vehiclebooking = models.ForeignKey(VehicleBooking, related_name='monthlypayment')

# 	class Meta:
# 		verbose_name = "MonthlyPayment"
# 		verbose_name_plural = "MonthlyPayments"

# 	def __str__(self):
# 		return self.monthly
