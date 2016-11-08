from django import forms
from django.contrib.auth.models import User
from clients.models import Client

class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label="Password", widget=forms.PasswordInput)
	password2 = forms.CharField(label="Repeat your Password", widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'email')

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