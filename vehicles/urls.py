from django.conf.urls import url
from . import views


urlpatterns =[


	url(r'^$',views.Vehicles.as_view(), name= 'catalog'),

]
