from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),    
path('stalls', views.stall_list, name='stall_list'),
path('<int:stall_id>/', views.stall_detail, name='stall_detail'),
path('stall/<int:stall_id>/dashboard/', views.stall_dashboard, name='stall_dashboard'),
path('order/<int:order_id>/ready/', views.mark_order_ready, name='mark_order_ready'),
path('cart/', views.view_cart, name='view_cart'),
path('checkout/', views.checkout, name='checkout'),
path('cart/update/<int:menu_item_id>/', views.update_cart_item, name='update_cart_item'),
path('blogs/', views.blogs, name='blogs'),
path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
path('contacts/', views.contacts, name='contacts'),
]
