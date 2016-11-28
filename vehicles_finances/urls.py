from django.conf.urls import url, include
from . import views




urlpatterns = [

	url(r'^contratos/$', views.contratList.as_view(), name='agreement'),
	url(r'^contratos/detallePagos', views.detailPayments.as_view(), name='detailPayment'),

]
