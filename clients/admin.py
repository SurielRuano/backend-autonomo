from django.contrib import admin
from .models import Client, Garage
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
	# list_display = ('phone_num',)
	list_filter = ('rfc', 'curp',)
	search_fields = ('rfc', 'curp',)
	ordering = ['rfc']

class GarageAdmin(admin.ModelAdmin):
	list_display = ('user_garage',)
	list_filter = ('user_vehicle',)
	search_fields = ('user_garage',)

admin.site.register(Client, ClientAdmin)
admin.site.register(Garage, GarageAdmin)