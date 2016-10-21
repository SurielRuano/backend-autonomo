from __future__ import unicode_literals
 
from django.db import models



class CarModel(models.Model):
	name = models.CharField(max_length=60)
	anio = models.DateField(auto_now=True)
	doors_num = models.IntegerField (max_length=2);
	cylinders_num = models.IntegerField(max_length=2)
	description_short = models.TextField() 
	description_long = models.TextField()
	img_front = models.ImageField(upload_to="autos/img_front" blank=True null=True)
	img_left = models.ImageField(upload_to="autos/img_left" blank=True null=True)
	img_right = models.ImageField(upload_to= "autos/img_right" blank=True, null=True)
	img_back = models.ImageField(upload_to= "autos/img_back" blank=True, null=True)
	car_line = models.CharField(max_length=50)
	price = models.FloatField()

	def __str__(self):
		return 'Auto {}'.format(self.name)


# Create your models here.
