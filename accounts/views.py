from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserRegistrationForm

# Create your views here.
class Registration (View):
	def get(self, request):
		template_name = "registration/registry"
		form = UserRegistrationForm()
		context = {
		'form':form,
		}
		return render(request, template_name, context)
