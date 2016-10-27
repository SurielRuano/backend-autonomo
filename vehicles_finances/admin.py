from django.contrib import admin
from .models import VehicleBooking, MonthlyPayment

# Register your models here.

admin.site.register(VehicleBooking)
admin.site.register(MonthlyPayment)