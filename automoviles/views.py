from django.shortcuts import render
from django.views.generic import View


class Autos(View):

	def get(self,request):

		template_name = 'autos/autos.json'

		return render(request, template_name)


