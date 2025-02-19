from django.shortcuts import render, redirect, get_object_or_404

# Authentication 
from django.contrib.auth.decorators import login_required

# Model
from OrderApp.models import Cart, Order
from ShopApp.models import Product

# Message
from django.contrib import messages


# Create your views here.

@login_required
def add_to_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_item = Cart.objects.get_or_create(item=item, user=request.user, purchased=False) 
    
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    
    if order_qs.exists():
        order = order_qs[0]
        
        if order.orderItems.filter(item=item).exists():
            order_item [0].quantity += 1
            order_item[0].save()
            messages.info(request, "This item quantity was updated.")
            return redirect("shop_app:home")
        else:
            order.orderItems.add(order_item[0])
            messages.info(request, "This item was added to you cart")
            return redirect("shop_app:home")
    else:
        order = Order(user=request.user)
        order.save()
        order.orderItems.add(order_item[0])
        messages.info(request, "This item was added to cart.")
        return redirect("shop_app:home")

@login_required
def cart_view(request):
    carts = Cart.objects.filter(user=request.user, purchased=False)
    orders = Order.objects.filter(user=request.user, ordered=False)
    
    if carts.exists() and orders.exists():
        order = orders[0]
        return render(request, 'OrderApp/cart.html', context={'carts':carts, 'order':order})
    else:
        messages.warning(request, "You don't have any item in your cart!")
        return redirect('shop_app:home')
    
    