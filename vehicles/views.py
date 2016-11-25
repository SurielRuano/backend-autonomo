from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import View
from .models import Vehicle, Vehicle_version, trademark
from vehicles_finances.models import SettingsFinantial
from clients.models import Client, Garage
from django.contrib.auth.models import User
from django.core import serializers
from django.contrib.auth.forms import AuthenticationForm
#librerias para paginacion
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
## librearias para autentificacion
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required




class Vehicles(View):

	def get(self,request):

		template_name = 'catalog/catalog.html'

		queryset = Vehicle.objects.filter(publication_status='published')

		paginator = Paginator(queryset,9)
		page = request.GET.get('page')

		try:

			vehicles = paginator.page(page)

		except PageNotAnInteger:

			vehicles = paginator.page(1)

		except EmptyPage:

			vehicles = paginator.page(paginator.num_pages)


		# [list(Vehicle.tobjects.all()) for Vehicle in queryset]

		#context = {'datos':serializers.serialize("json", queryset)}
		context = {'vehicles':vehicles,'pages':page}


		return render(request, template_name, context)



class Detail(View):

	def get(self,request,id):

		template_name = 'vehicle_detail/detail.html'

		vehicle = Vehicle.objects.get(pk=id)


		version = Vehicle_version.objects.all().filter(vehicle = vehicle)

		context = {'vehicle':vehicle, 'version':version,'form_login':AuthenticationForm()}



		return render(request, template_name, context)



class AddToGarage(View):

	

	def get(self,request,id_version,mounths):



		version = Vehicle_version.objects.get(pk=id_version)
		current_user = request.user
		client = Client.objects.get(user_client = current_user.id)

		g = Garage.objects.create(user_garage=client,user_vehicle=version,monthly_payment=mounths)

		g.save()

		return redirect('accounts:profile')




"""
	login con ajax jquery
"""

class LoginAjax(View):

	def post(self,request):

		if request.method == 'POST':

			username = request.POST['username']
			password = request.POST['password']
			id_vehicle = request.POST['vehicle']
			mounths = request.POST['mounth']

			user = authenticate(username=username,password=password)


			if user is not None:

				login(request,user)

				version = Vehicle_version.objects.get(pk=id_vehicle)
				current_user = request.user
				client = Client.objects.get(user_client = current_user.id)

				g = Garage.objects.create(user_garage=client,user_vehicle=version,monthly_payment=mounths)

				g.save()

				return HttpResponse(True)

			else:

				return HttpResponse(False)

		else:

			return HttpResponse(False)


		







