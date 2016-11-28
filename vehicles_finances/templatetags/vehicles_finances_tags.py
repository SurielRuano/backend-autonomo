from django import template
register = template.Library()
from ..models import DetailPayment, Agreement


## tag que recibe una variable y renderiza un pequeno template html
@register.inclusion_tag('template_tags/detail_payments.html',takes_context=True)
def show_payments(context,count=6):
	request = context['request']
	payments= DetailPayment.objects.all()[:count]
	user_id = request.user.email
	return {
	'payments':payments, 'user_id': user_id 
	}