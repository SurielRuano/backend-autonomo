from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Client(models.Model):
	full_name = models.CharField(max_length=120)
	address = models.TextField()
	email = models.EmailField()
	phone_num = models.CharField(max_length=12)
	birthday = models.DateField()
	rfc = models.CharField(max_length=13)
	curp = models.CharField(max_lenght=18)
	gender = models.CharField(max_lenght=40)
	nationality = models.CharField(max_lenght=100)
	marital_status = models.CharField(max_lenght=40)
	scholarship = models.CharField(max_lenght=40)
	ocuppation = models.CharField(max_length=200)
	salary = models.FloatField()
	personale_references = models.TextField()

	class Meta:
		verbose_name="Client"
		verbose_name_plural = "Clients"

	def __str__(self):
		return 'Cliente {}'.format(self.full_name)