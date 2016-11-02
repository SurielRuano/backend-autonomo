from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from vehicles.models import Vehicle
from django.conf import settings


# Create your models here.
class Client(models.Model):
	user_client = models.OneToOneField(settings.AUTH_USER_MODEL)
	address = models.TextField()
	phone_num = models.CharField(max_length=12)
	birthday = models.DateField()
	rfc = models.CharField(max_length=13)
	curp = models.CharField(max_length=18)
	gender = models.CharField(max_length=40)
	nationality = models.CharField(max_length=100)
	marital_status = models.CharField(max_length=40)
	scholarship = models.CharField(max_length=40)
	ocuppation = models.CharField(max_length=200)
	salary = models.FloatField()
	personale_references = models.TextField()

	class Meta:
		verbose_name="Client"
		verbose_name_plural = "Clients"

	def __str__(self):
		return 'Cliente {}'.format(self.user_client)


class Garage(models.Model):
	user_garage = models.ForeignKey(Client, related_name='garage')
	user_vehicle = models.ForeignKey(Vehicle, related_name='garage')

	class Meta:
		verbose_name = "Garage"
		verbose_name_plural = "Garages"

	def __str__(self):
		return 'Garage numero {}'.format(self.id)