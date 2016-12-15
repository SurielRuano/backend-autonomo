from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm, ProofForm, VehicleFormVersion
from django.contrib.auth.models import User
from clients.models import Client, Garage
from vehicles.models import Vehicle_version
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from vehicles_finances.models import Agreement, groups_stockExchange


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
		#bajo el formulario para obtener el identificador de el vehiculo
		vehicle_garage =  VehicleFormVersion()
		# profile = ProfileEditForm(instance=request.user.client)
		profile = Client.objects.get(user_client=request.user)
		client = Client.objects.get(user_client=request.user)
		garage = Garage.objects.all().filter(user_garage=client)
		context = {
		'userform':userform,
		'profile':profile,
		'garage': garage,
		'proof' : proof,
		'vehicle_garage': vehicle_garage,		
		}
		return render(request, template_name, context)

	def post(self,request):
		id_vehicle = request.POST['id_vehicle_version']
		print("Aqui esta el valor: " + id_vehicle)
		template_name = "registration/profile.html"
		proof = ProofForm(instance=request.user.client, data=request.POST)

		if proof.is_valid():
			proof.save()
			vehicle_ver = Vehicle_version.objects.get(id=id_vehicle)
			group_stock = groups_stockExchange(unique_id='da135554-fe71-409e-bfc3-7380d4a1518c')
			client = Client.objects.get(user_client=request.user)
			agrement = Agreement.objects.create(id_client=client, id_vehicle_version=vehicle_ver, groups_stockexchange = group_stock)
			agrement.save()
			return redirect('accounts:profile')
		else:
			return redirect('home')

		# #client_form = ProofForm()
		# proof = ProofForm(instance=request.user.client, data=request.POST)
		# vehicle_garage = VehicleFormVersion(data=request.POST)
		# #bajar modelo
		# contrato = Agreement()
		# if proof.is_valid() and vehicle_garage.is_valid():
		# 	proof.save()
		# 	vehicle = vehicle_garage.save(commit=False)


		# 	client = Client.objects.get(user_client=request.user)
		# 	carro_garage = Garage.objects..all().filter(user_garage = client)
		# 	car_agreement = carro_garage.objects.get(carro_garage.id = vehicle.vehicle_garage)

		# 	contrato.unique_id = 658941236587456398512548
		# 	contrato.zone = 'Pachuca'
		# 	contrato.observations = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod"
		# 	contrato.status = True
		# 	contrato.id_client = request.user.client
		# 	contrato.id_vehicle_version = 
		# 	return redirect('home')
		# else:
		# 	context = {
		# 	'proof':proof
		# 	}
			# return render(request, template_name)
		return redirect ('accounts:profile')