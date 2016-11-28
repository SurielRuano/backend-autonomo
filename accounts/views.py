from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm, ProofForm
from django.contrib.auth.models import User
from clients.models import Client, Garage
from vehicles.models import Vehicle_version
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


##Para utilizar el PDF
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint

# @staff_member_required
def admin_order_pdf(request, info_id):
	client = get_object_or_404(Client, id=info_id)
	html = render_to_string('pdf/pdf.html', {'client':client})
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'file_name = \
		"cliente_{}.pdf"'.format(client.id)
	weasyprint.HTML(string=html).write_pdf(response,
		stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + '/css/pdf.css')])
	return response


		# stylesheets=[weasyprint.CSS(
		# 	settings.STATIC_URL + 'pdfs/contratos.css')]



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
			return render(request, template_name, context)


class ProfileView(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name= "registration/profile.html"
		proof = ProofForm(instance=request.user.client)
		userform = UserEditForm(instance=request.user)
		profile = ProfileEditForm(instance=request.user.client)
		client = Client.objects.get(user_client=request.user)
		garage = Garage.objects.all().filter(user_garage=client)
		context = {
		'userform':userform,
		'profile':profile,
		'garage': garage,
		'proof' : proof,		}
		return render(request, template_name, context)

	def post(self,request):
		template_name = "registration/profile.html"
		#client_form = ProofForm()
		proof = ProofForm(instance=request.user.client, data=request.POST)
		if proof.is_valid():
			proof.save()
			return redirect('home')
		else:
			context = {
			'proof':proof
			}
			return render(request, template_name,context)