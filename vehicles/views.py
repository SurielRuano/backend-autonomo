from django.shortcuts import render
from django.views.generic import View
from .models import Vehicle, vehicle_color
from django.core import serializers



class Vehicles(View):

	def get(self,request):

		template_name = 'vehicles/vehicles.json'

		queryset = Vehicle.objects.all()

		# [list(Vehicle.tobjects.all()) for Vehicle in queryset]

		context = {'datos':serializers.serialize("json", queryset)}


		return render(request, template_name, context)
