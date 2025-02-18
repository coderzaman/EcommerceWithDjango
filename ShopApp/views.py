from django.shortcuts import render

# Import Views
from django.views.generic import ListView, DeleteView 

# Import Models
from .models import Product

# Create your views here.

class home(ListView):
    model = Product
    template_name = 'ShopApp/home.html'