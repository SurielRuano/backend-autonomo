import sys
sys.stdout.buffer.write(("|\t "+ chr(9986) +" PySnipt'd " + chr(9986)+" \t|").encode('utf8'))

from requests import request, ConnectionError
from clients.models import Client
# from mailin import mails
 
def save_profile_picture(backend, user, response, is_new,  *args, **kwargs):
	if backend.name == 'facebook' and is_new:
		user_model=user
		user_profile=Client()
		user_profile.user_client=user_model
		# url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
		ide=response['id']
		correo=response['email']
		print(ide)


		try:
			user_profile.ide=ide
			user_profile.save()

		except ConnectionError:
			pass
			print("Error de conexion")
	# # Dando bienvenida
	# 	try:
	# 		datos={
	# 		'usuario':user
	# 		}
	# 		mails.welcome_mail(datos,correo)
	# 	except:
	# 		print("error en envio")