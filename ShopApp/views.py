from django.shortcuts import render

# Import Views
from django.views.generic import ListView, DetailView 

# Import Models
from .models import Product

#Mixin
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class home(ListView):
    model = Product
    template_name = 'ShopApp/home.html'
    

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'ShopApp/product.html'