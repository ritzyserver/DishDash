from django.shortcuts import render, get_object_or_404, redirect
from .models import Stall, MenuItem, Order, Recipe
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Home page view (public)
def home(request):
    stalls = Stall.objects.all()
    return render(request, 'orders/home.html', {'stalls': stalls})

# Stall list view (public)
def stall_list(request):
    stalls = Stall.objects.all()
    return render(request, 'orders/stall_list.html', {'stalls': stalls})

# Stall detail and order creation view
def stall_detail(request, stall_id):
    stall = get_object_or_404(Stall, id=stall_id)
    success_message = None
    show_auth_form = False
    auth_error = None

    if request.method == 'POST':
        # Unauthenticated users: show login/signup form
        if not request.user.is_authenticated:
            show_auth_form = True
            action = request.POST.get("action")

            if action == "login":
                username = request.POST.get("username")
                password = request.POST.get("password")
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    return redirect(request.path)  # retry after login
                else:
                    auth_error = "Invalid login credentials."

            elif action == "signup":
                username = request.POST.get("username")
                password = request.POST.get("password")
                if User.objects.filter(username=username).exists():
                    auth_error = "Username already exists."
                else:
                    user = User.objects.create_user(username=username, password=password)
                    login(request, user)
                    return redirect(request.path)

        # Authenticated users: process the order
        else:
            customer_name = request.user.username
            menu_item_id = request.POST.get('menu_item_id')
            delivery_type = request.POST.get('delivery_type')
            quantity = int(request.POST.get('quantity', 1))
            menu_item = get_object_or_404(MenuItem, id=menu_item_id)
            Order.objects.create(
                menu_item=menu_item,
                customer_name=customer_name,
                delivery_type=delivery_type,
                quantity=quantity,
                is_paid=False,
                is_ready=False
            )
            success_message = "Items added to Cart !"

    return render(request, 'orders/stall_detail.html', {
        'stall': stall,
        'success_message': success_message,
        'show_auth_form': show_auth_form,
        'auth_error': auth_error
    })

# Dashboard for stall staff - protected
@login_required
def stall_dashboard(request, stall_id):
    stall = get_object_or_404(Stall, id=stall_id)
    orders = Order.objects.filter(menu_item__stall=stall).order_by('-id')
    return render(request, 'orders/stall_dashboard.html', {'stall': stall, 'orders': orders})

# Mark an order ready - protected
@login_required
def mark_order_ready(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.is_ready = True
    order.save()
    return JsonResponse({'status': 'success'})

# View Cart
@login_required
def view_cart(request):
    orders = Order.objects.filter(customer_name=request.user.username, is_paid=False)
    
    # Group orders by menu item and stall
    grouped_orders = {}
    for order in orders:
        key = (order.menu_item.id, order.menu_item.stall.id)
        if key in grouped_orders:
            grouped_orders[key]['quantity'] += order.quantity
            grouped_orders[key]['total'] += order.menu_item.price * order.quantity
        else:
            grouped_orders[key] = {
                'menu_item': order.menu_item,
                'stall': order.menu_item.stall,
                'quantity': order.quantity,
                'total': order.menu_item.price * order.quantity
            }
    
    grouped_orders = list(grouped_orders.values())
    return render(request, 'orders/cart.html', {'grouped_orders': grouped_orders})

@login_required
def update_cart_item(request, menu_item_id):
    if request.method == 'POST':
        action = request.POST.get('action')
        orders = Order.objects.filter(
            customer_name=request.user.username,
            menu_item_id=menu_item_id,
            is_paid=False
        )
        
        if action == 'increase':
            # Add new order with quantity 1
            menu_item = get_object_or_404(MenuItem, id=menu_item_id)
            Order.objects.create(
                menu_item=menu_item,
                customer_name=request.user.username,
                quantity=1,
                is_paid=False
            )
        elif action == 'decrease':
            # Remove one order
            if orders.exists():
                orders.first().delete()
        elif action == 'remove':
            # Remove all orders of this item
            orders.delete()
            
    return redirect('view_cart')

# Checkout
@login_required
def checkout(request):
    orders = Order.objects.filter(customer_name=request.user.username, is_paid=False)
    
    # Group orders by menu item and stall
    grouped_orders = {}
    for order in orders:
        key = (order.menu_item.id, order.menu_item.stall.id)
        if key in grouped_orders:
            grouped_orders[key]['quantity'] += order.quantity
            grouped_orders[key]['total'] += order.menu_item.price * order.quantity
        else:
            grouped_orders[key] = {
                'menu_item': order.menu_item,
                'stall': order.menu_item.stall,
                'quantity': order.quantity,
                'total': order.menu_item.price * order.quantity
            }
    
    grouped_orders = list(grouped_orders.values())
    total_amount = sum(item['total'] for item in grouped_orders)

    if request.method == 'POST':
        for order in orders:
            order.is_paid = True
            order.save()
        return render(request, 'orders/payment_success.html')

    return render(request, 'orders/checkout.html', {
        'grouped_orders': grouped_orders,
        'total_amount': total_amount
    })
def blogs(request):
    recipes = Recipe.objects.all().order_by('-created_at')
    return render(request, 'orders/blogs.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'orders/recipe_detail.html', {'recipe': recipe})

def contacts(request):
    stalls = Stall.objects.all()
    return render(request, 'orders/contacts.html', {'stalls': stalls})
