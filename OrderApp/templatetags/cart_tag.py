from django import template
from OrderApp.models import Order

register = template.Library()

@register.filter
def cart_total(user):
    order = Order.objects.filter(user=user, ordered = False)
    
    if order.exists():
        return order[0].orderItems.count()
    else:
        return 0