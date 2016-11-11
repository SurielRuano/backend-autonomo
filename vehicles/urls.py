from django.conf.urls import url
from . import views


urlpatterns =[


	url(r'^$',views.Vehicles.as_view(), name= 'catalog'),
	url(r'^detalle/(?P<id>\d+)/$',views.Detail.as_view(), name= 'detail'),
	url(r'^agregarG/(?P<id_version>\d+)/(?P<mounths>\d+)$',views.AddToGarage.as_view(), name= 'agregarG'),

]
