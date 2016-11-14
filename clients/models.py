from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from vehicles.models import Vehicle_version
from django.conf import settings


# Create your models here.
class Client(models.Model):
	BOOL_CHOICES = ((True, 'Activo'), (False, 'Inactivo'))
	user_client = models.OneToOneField(settings.AUTH_USER_MODEL)
	address = models.TextField(blank=True, null=True)
	phone_num = models.CharField(max_length=12, blank=True, null=True)
	birthday = models.DateField(blank=True, null=True)
	rfc = models.CharField(max_length=13, blank=True, null=True)
	curp = models.CharField(max_length=18, blank=True, null=True)
	gender = models.CharField(max_length=40, blank=True, null=True)
	nationality = models.CharField(max_length=100, blank=True, null=True)
	marital_status = models.CharField(max_length=40, blank=True, null=True)
	scholarship = models.CharField(max_length=40, blank=True, null=True)
	ocuppation = models.CharField(max_length=200, blank=True, null=True)
	salary = models.FloatField(blank=True, null=True)
	personale_references = models.TextField(blank=True, null=True)
	user_status = models.BooleanField(choices = BOOL_CHOICES, default=False)
	photo = models.ImageField(upload_to="users", blank=True, null=True)

	class Meta:
		verbose_name="Client"
		verbose_name_plural = "Clients"

	def __str__(self):
		return 'Cliente {}'.format(self.user_client)


class Garage(models.Model):
	user_garage = models.ForeignKey(Client, related_name='garage')
	user_vehicle = models.ForeignKey(Vehicle_version, related_name='garage')
	monthly_payment = models.IntegerField(blank=True, null=True)
	status  = models.BooleanField(default=False)
	add_date = models.DateField(auto_now=True)

	class Meta:
		verbose_name = "Garage"
		verbose_name_plural = "Garages"

	def __str__(self):
		return 'Garage numero {}'.format(self.id)