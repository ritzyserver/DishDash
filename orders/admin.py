from django.contrib import admin

# Register your modfrom django.contrib import admin
from .models import Stall, MenuItem, Order

# Registering models to the admin panel
admin.site.register(Stall)
admin.site.register(MenuItem)
admin.site.register(Order)

# @admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'menu_item', 'customer_name', 'status', 'is_paid', 'is_ready')
    list_filter = ('status', 'is_ready', 'is_paid')
    search_fields = ('customer_name', 'menu_item__name')



