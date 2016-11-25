from django.contrib import admin
from .models import  DetailPayment, StockExchange, groups_stockExchange, SettingsFinantial, Agreement

# Register your models here.


class DetailPaymentAdmin (admin.ModelAdmin):
	list_display=('payment_reference', 'date_payment',)
	list_filter =('payment_reference', 'date_payment',)
	search_fields = ('payment_reference', 'date_payment', 'concept',)
	ordering = ['date_payment']

class StockExchangeAdmin (admin.ModelAdmin):
	list_display=('monthly',)
	list_filter =('monthly',)
	search_fields = ('monthly',)



admin.site.register(DetailPayment, DetailPaymentAdmin)
admin.site.register(StockExchange, StockExchangeAdmin)
admin.site.register(groups_stockExchange)
admin.site.register(SettingsFinantial)
admin.site.register(Agreement)
