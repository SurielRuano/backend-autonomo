from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.models import User
from clients.models import Client, Garage
from vehicles.models import Vehicle_version
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.
class RegistryView (View):
	def get(self, request):
		template_name = "registration/registry.html"
		form = UserRegistrationForm()
		context = {
		'form':form,
		}
		return render(request, template_name, context)

	def post(self,request):
		template_name = "registration/registry.html"
		new_user_f = UserRegistrationForm(request.POST)
		if new_user_f.is_valid():
			new_user = new_user_f.save(commit=False)
			new_user.set_password(new_user_f.cleaned_data['password'])
			new_user.save()
			client = Client()
			client.user_client = new_user
			client.save()
			return redirect('accounts:login')
		else:
			context = {
			'form':new_user_f,
			}
			return redirect(request, template_name, context)


class ProfileView(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name= "registration/profile.html"
		userform = UserEditForm(instance=request.user)
		profile = ProfileEditForm(instance=request.user.client)
		client = Client.objects.get(user_client=request.user)
		garage = Garage.objects.all().filter(user_garage=client)
		context = {
		'userform':userform,
		'profile':profile,
		'garage': garage,
		}
		return render(request, template_name, context)