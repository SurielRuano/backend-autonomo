from django.shortcuts import render
from django.views import View

from django.contrib.auth.models import User
from clients.models import Client
from vehicles_finances.models import Agreement, DetailPayment



# Create your views here.

class contratList(View):


	def get(self,request):


		template_name = 'client/profile/agreements.html'


		user = request.user
		client = Client.objects.get(user_client = user)
		agreements = Agreement.objects.filter(id_client = client)

		context = {'agreements':agreements}


		return render(request,template_name, context)



class detailPayments(View):


	def get(self,request):


		template_name = 'client/profile/detail_payments.html'

		user = request.user
		client = Client.objects.get(user_client = user)

		payments= DetailPayment.objects.all()

		context = {'payments':payments}


		return render(request,template_name, context)


