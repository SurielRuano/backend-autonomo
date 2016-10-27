from django.contrib import admin

from .models import Vehicle, Vehicle_version, trademark

# Register your models here.


admin.site.register(Vehicle)
admin.site.register(Vehicle_version)
admin.site.register(trademark)