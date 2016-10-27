from django.shortcuts import render
from django.views.generic import View
from .models import Vehicle
from django.core import serializers



class Vehicles(View):

	def get(self,request):

		template_name = 'vehicles/vehicles_json.html'
		context = {'datos':serializers.serialize("json", Vehicle.objects.all())}

		return render(request, template_name, context)
