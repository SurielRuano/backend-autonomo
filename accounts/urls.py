from django.conf.urls import url, include
from django.contrib.auth.views import login, logout
from . import views
from vehicles_finances import urls as urlsAgreement
urlpatterns = [
	url(r'^profile/$', views.ProfileView.as_view(), name="profile"),
	url(r'^registry/$', views.RegistryView.as_view(), name="registry"),
	url(r'^login/$', login, name="login"),
	url(r'^logout/$', logout,{'next_page': '/'}, name="logout" ),
	url(r'^cliente/(?P<info_id>\d+)/pdf/$', views.admin_order_pdf, name='cliente'),
	url(r'^profile/', include(urlsAgreement, namespace="profile2")),
]