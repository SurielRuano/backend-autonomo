from django.shortcuts import render
from django.views.generic import View
from .models import Car
from django.core import serializers



class Autos(View):

	def get(self,request):

		template_name = 'automoviles/automoviles.html'
		context = {'datos':serializers.serialize("json", Car.objects.all())}

		return render(request, template_name, context)


