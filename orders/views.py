from django.shortcuts import render, get_object_or_404
from .models import Stall, MenuItem, Order
from django.http import JsonResponse


# Home page view
def home(request):
    stalls = Stall.objects.all()  # Get all the stalls
    return render(request, 'orders/home.html', {'stalls': stalls})

# Stall list view
def stall_list(request):
    stalls = Stall.objects.all()
    return render(request, 'orders/stall_list.html', {'stalls': stalls})

# Stall detail and order creation view
def stall_detail(request, stall_id):
    stall = get_object_or_404(Stall, id=stall_id)

    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        menu_item_id = request.POST.get('menu_item_id')
        delivery_type = request.POST.get('delivery_type')
        quantity = int(request.POST.get('quantity', 1))
        menu_item = get_object_or_404(MenuItem, id=menu_item_id)

        Order.objects.create(
            menu_item=menu_item,
            customer_name=customer_name,
            delivery_type=delivery_type,
            is_paid=True,  # You can change this based on payment logic
            is_ready=False
        )

        # You can redirect or show a success message here
        return render(request, 'orders/order_success.html', {
            'stall': stall,
            'customer_name': customer_name,
            'menu_item': menu_item
        })

    return render(request, 'orders/stall_detail.html', {'stall': stall})
def stall_dashboard(request, stall_id):
    stall = get_object_or_404(Stall, id=stall_id)
    orders = Order.objects.filter(menu_item__stall=stall).order_by('-id')
    return render(request, 'orders/stall_dashboard.html', {'stall': stall, 'orders': orders})

# @require_POST
def mark_order_ready(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.is_ready = True
    order.save()
    return JsonResponse({'status': 'success'})
