from django.contrib import admin

from .models import Vehicle, Vehicle_version, trademark

# Register your models here.

class DetalleVehiculos(admin.ModelAdmin):

	list_display=('name','trademark','publication_status')
	list_filter= ('trademark','publication_status')
	search_fields = ('name','trademark')
	prepopulated_fields = {"v_slug": ("name",)}


class trademarkl(admin.ModelAdmin):

	model = Vehicle
	list_display  = ('version','vehicle','trademark2')
	search_fields = ('version','vehicle__name','vehicle__trademark__name')
	list_filter = ('vehicle__trademark',)






	def trademark2(self,obj):
		return obj.vehicle.trademark

	trademark2.short_description = 'Trademark'



admin.site.register(Vehicle,DetalleVehiculos)
admin.site.register(Vehicle_version,trademarkl)
admin.site.register(trademark)