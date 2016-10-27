from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Clients(models.Model):
	user_name = models.CharField()