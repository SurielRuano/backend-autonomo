from django.shortcuts import render
from django.views.generic import View


class Autos(View):

	def get(self,request):

		template_name = 'automoviles/automoviles.html'

		return render(request, template_name)


