from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import View
from .models import Vehicle, Vehicle_version, trademark
from vehicles_finances.models import SettingsFinantial
from clients.models import Client, Garage
from django.contrib.auth.models import User
from django.core import serializers
from django.contrib.auth.forms import AuthenticationForm



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

		vehicle = Vehicle.objects.filter(pk=id)


		version = Vehicle_version.objects.all().filter(vehicle = vehicle)

		context = {'vehicle':vehicle, 'version':version,'form_login':AuthenticationForm()}



		return render(request, template_name, context)



class AddToGarage(View):

	

	def get(self,request,id_version):



		version = Vehicle_version.objects.get(pk=id_version)
		current_user = request.user
		client = Client.objects.get(user_client = current_user.id)

		g = Garage.objects.create(user_garage=client,user_vehicle=version)

		g.save()

		return redirect('accounts:profile')




