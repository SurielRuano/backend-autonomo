from django.db import models

# Create your models here.


class Cliente(models.Model):

	nombre_completo = models.CharField(max_length=120)
	fecha_nacimiento = models.DateField()
	telefono = models.CharField(max_length=12)
	