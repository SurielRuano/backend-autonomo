from django import template
register = template.Library()
from ..models import DetailPayment


## tag que recibe una variable y renderiza un pequeno template html
@register.inclusion_tag('template_tags/detail_payments.html')
def show_payments(count=6):
	payments= DetailPayment.objects.all()[:count]
	return {
	'payments':payments
	}