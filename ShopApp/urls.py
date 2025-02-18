from django.urls import path
from . import views

app_name = 'shop_app'

urlpatterns = [
    path('', view=views.home.as_view(), name='home' ),
    path('product/<pk>/', view=views.ProductDetail.as_view(), name='product' ),
]
