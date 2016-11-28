from django.contrib import admin
from .models import Client, Garage
from django.core.urlresolvers import reverse
# Register your models here.

def client_pdf(obj):
	return '<a href="{}">PDF</a>'.format(
		reverse('accounts:cliente', args=[obj.id]))
	client_pdf.allow_tags = True
	client_pdf.short_description = 'PDF hugo'

class ClientAdmin(admin.ModelAdmin):
	list_display = (client_pdf,)
	list_filter = ('rfc', 'curp',)
	search_fields = ('rfc', 'curp',)
	ordering = ['rfc']

class GarageAdmin(admin.ModelAdmin):
	list_display = ('user_garage',)
	list_filter = ('user_vehicle',)
	search_fields = ('user_garage',)

admin.site.register(Client, ClientAdmin)
admin.site.register(Garage, GarageAdmin)