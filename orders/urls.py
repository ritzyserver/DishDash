from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),    
path('', views.stall_list, name='stall_list'),
path('<int:stall_id>/', views.stall_detail, name='stall_detail'),
path('stall/<int:stall_id>/dashboard/', views.stall_dashboard, name='stall_dashboard'),
path('order/<int:order_id>/ready/', views.mark_order_ready, name='mark_order_ready'),
]

