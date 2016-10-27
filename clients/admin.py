from django.contrib import admin
from .models import Client
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
	list_display = ('full_name', 'email', 'phone_num')
	list_filter = ('full_name', 'email')
	search_fields = ('full_name', 'email', 'rfc')
	ordering = ['full_name']


admin.site.register(Client, ClientAdmin)
