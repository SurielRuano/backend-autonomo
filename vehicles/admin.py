from django.contrib import admin

from .models import Vehicle, Vehicle_version, trademark

# Register your models here.

class DetalleVehiculos(admin.ModelAdmin):

	list_display=('name','trademark','publication_status')
	list_filter= ('trademark','publication_status')
	search_fields = ('name','trademark')



admin.site.register(Vehicle,DetalleVehiculos)
admin.site.register(Vehicle_version)
admin.site.register(trademark)