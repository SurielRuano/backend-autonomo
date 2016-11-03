from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserRegistrationForm

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
			return redirect('home')
		else:
			context = {
			'form':new_user_f,
			}
			return redirect(request, template_name, context)