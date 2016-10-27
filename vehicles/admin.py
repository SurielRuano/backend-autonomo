from django.contrib import admin

from .models import Vehicle, Vehicle_version, trademark, vehicle_color

# Register your models here.


admin.site.register(Vehicle)
admin.site.register(Vehicle_version)
admin.site.register(vehicle_color)
admin.site.register(trademark)