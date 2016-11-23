from django import forms
from django.contrib.auth.models import User
from clients.models import Client

CHOICES = (('Ho','Hombre'), ('Mu','Mujer'))
CHOICESM = (('casado', 'Casado'), ('soltero', 'Soltero'))

class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label="Password", widget=forms.PasswordInput)
	password2 = forms.CharField(label="Repeat your Password", widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'email')
		help_texts = {
            'username': None,
        }

	def clean_password2(self):
		clean = self.cleaned_data
		if clean ['password'] != clean['password2']:
			raise forms.ValidationError("Passwords don't match")
		return clean['password2']


class UserEditForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
	class Meta:
		model = Client
		fields = (
			'address',
			'phone_num',
			'birthday',
			'rfc',
			'curp',
			'gender',
			'nationality',
			'marital_status',
			'scholarship',
			'ocuppation',
			'salary',
			'personale_references',
			)

class ProofForm(forms.ModelForm):

    address = forms.CharField(label="Dirección", widget=forms.TextInput(attrs={'class' : 'form-control', 
    	'type' : 'text', 
    	'placeholder' : 'Dirección' }))

    phone_num = forms.IntegerField(label="Número Telefónico", widget=forms.TextInput(attrs={'class' : 'form-control', 
    	'type' : 'number', 
    	'placeholder' : 'Número Telefónico'}))

    birthday = forms.DateTimeField(label="Fecha de nacimiento", widget=forms.TextInput(attrs={'class' : 'form-control'}))

    rfc = forms.CharField(label="RFC", widget=forms.TextInput(attrs={'class' : 'form-control', 
    	'type' : 'text', 
    	'placeholder': 'RFC'}))

    curp =  forms.CharField(label="Curp", widget=forms.TextInput(attrs = {'class' : 'form-control', 
    	'type' : 'text', 
    	'placeholder' : 'Curp'}))

    gender = forms.ChoiceField(choices = CHOICES, label='Sexo', widget=forms.Select(attrs = {'class' : 'form-control'}))

    nationality = forms.CharField(label="Nacionalidad", widget=forms.TextInput(attrs = {'class' : 'form-control',
    	'type' : 'text',
    	'placeholder' : 'Nacionalidad'}))

    marital_status = forms.ChoiceField(choices = CHOICESM, label="Estado Civil", widget = forms.Select(attrs = {'class' : 'form-control'}))
    
    scholarship = forms.CharField(label="Escolaridad", widget = forms.TextInput(attrs = {'class' : 'form-control', 
    	'type' : 'text',
    	'placeholder' : 'Escolaridad'}))

    ocuppation = forms.CharField(label="Ocupación", widget = forms.TextInput(attrs = {'class' : 'form-control',
    	'placeholder' : 'Ocupación'}))

    salary = forms.CharField(label="Salario", widget=forms.TextInput(attrs = {'class' : 'form-control',
    	'type' : 'text',
    	'placeholder' : 'Salario'}))

    class Meta:
    	model = Client
    	fields = (
    		'address',
    		'phone_num',
    		'birthday',
    		'rfc',
    		'curp',
    		'gender',
    		'nationality',
    		'marital_status',
    		'scholarship',
    		'ocuppation',
    		'salary',
    		)