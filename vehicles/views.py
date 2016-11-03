from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Vehicle, Vehicle_version
from django.core import serializers



class Vehicles(View):

	def get(self,request):

		template_name = 'catalog/catalog.html'

		queryset = Vehicle.objects.all()

		# [list(Vehicle.tobjects.all()) for Vehicle in queryset]

		#context = {'datos':serializers.serialize("json", queryset)}
		context = {'vehicles':queryset}


		return render(request, template_name, context)



class Detail(View):

	def get(self,request,id):

		template_name = 'vehicle_detail/detail.html'

		queryset = Vehicle.objects.filter(pk=id)

		ver = Vehicle_version.objects.all().filter(vehicle = queryset)		
		
		# version = Vehicle_version.vehicle.all()
		
		context = {'vehicle':queryset, 'version':ver}


		return render(request, template_name, context)
