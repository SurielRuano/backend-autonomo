from django.contrib import admin
from .models import VehicleBooking, DetailPayment, StockExchange, SettingsFinantial

# Register your models here.
class VehicleBookingAdmin(admin.ModelAdmin):
	list_display=('id_client', 'id_stock', 'id_vehicle',)
	list_filter =('id_stock', 'adjudication',)
	search_fields = ('id_client', 'id_stock', 'id_vehicle','deadline',)
	ordering = ['id_client']

class DetailPaymentAdmin (admin.ModelAdmin):
	list_display=('reference_payment', 'date_payment',)
	list_filter =('reference_payment', 'date_payment',)
	search_fields = ('reference_payment', 'date_payment', 'concept',)
	ordering = ['date_payment']

class StockExchangeAdmin (admin.ModelAdmin):
	list_display=('name', 'maximum_number_customers', 'monthly_payment')
	list_filter =('maximum_number_customers', 'monthly_payment',)
	search_fields = ('name', 'maximum_number_customers', 'monthly_payment',)
	ordering = ['name']	

admin.site.register(VehicleBooking, VehicleBookingAdmin)
admin.site.register(DetailPayment, DetailPaymentAdmin)
admin.site.register(StockExchange, StockExchangeAdmin)
admin.site.register(SettingsFinantial)