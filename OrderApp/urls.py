from django.urls import path
from OrderApp import views

app_name = 'order_app'

urlpatterns = [
    path('add/<pk>/', view=views.add_to_cart, name='add'),
    path('cart/', view=views.cart_view, name='cart'),
]
